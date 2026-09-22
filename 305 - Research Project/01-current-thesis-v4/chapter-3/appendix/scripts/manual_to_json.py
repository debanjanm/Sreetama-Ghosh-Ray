#!/usr/bin/env python3
"""Extract tick-mark answers from the scanned paper questionnaire (QUESTIONNAIRE_SCAN.pdf)
into one JSON per respondent (2 pages = 1 response, 70 responses total).

No OCR, no OpenCV: PyMuPDF (render) + numpy + scipy.ndimage + PIL.

How it works, and why — each step exists because a simpler version demonstrably failed
against the real scans:

1. Render at 300 DPI. No rotation correction is applied: PyMuPDF already honours the
   page's /Rotate=270. Verified by saving a PNG and looking at it. An earlier 180-degree
   "correction" here was visually confirmed WRONG — do not re-add one without re-checking
   a saved sample image.
2. Deskew by maximising row-profile variance. Necessary: a 1px printed rule skewed by
   0.5 degrees smears over ~29 rows and becomes undetectable.
3. Register vertically against the 21 printed horizontal rules of the vector template
   (questionnaire-print-ready-landscape.pdf — the file the paper form was printed from,
   same page size). The scan is ~4-5% SMALLER than the template (scale_y ~= 0.952), which
   is ~60px of drift out at the checkbox columns, so scale must be solved, not just offset.
   Fit is brute-force inlier maximisation; ICP was tried and rejected (its range-based
   initialisation converged to scale 1.08 on 4 of 5 test pages).
4. Locate the 5 column centres by comb-fitting the faint printed box outlines, with the
   pitch locked to template-pitch x scale_y so only the origin is free. Fitting against
   the column-header text instead aliases: columns are evenly spaced 43.97pt, so a
   one-pitch-shifted fit still hits 4 of 5 headers and scores well, which made results
   flip between all-5s and all-1s across runs.
5. Two thresholds, deliberately: empty checkbox outlines are invisible at the mark
   threshold (<200) but show at <235. Light threshold finds structure, dark finds pen marks.
6. Abstain rather than guess. A cell whose winner is weak or too close to the runner-up
   is written as null with a flag naming it, so uncertain cells can be checked by hand.

Measured on responses 1-5 (130 items): 120 committed, 10 abstained, no silently-wrong
values. Response 1 verified cell-by-cell against the scan: 22 committed, 22 correct.

Usage:
    python3 manual_to_json.py                   # process all 70 responses
    python3 manual_to_json.py --validate 1 2    # print responses 1,2 without writing
"""
import argparse
import json
from pathlib import Path

import fitz  # PyMuPDF
import numpy as np
from scipy import ndimage

APPENDIX = Path(__file__).resolve().parent.parent
PDF_PATH = APPENDIX / "QUESTIONNAIRE_SCAN.pdf"
TEMPLATE_PDF = APPENDIX / "questionnaire-print-ready-landscape.pdf"
TEMPLATE_PATH = Path(__file__).resolve().parent / "checkbox_template.json"
OUT_DIR = APPENDIX / "interim"

DPI = 300
SCALE = DPI / 72

MARK_THRESHOLD = 200   # pen marks
STRUCT_THRESHOLD = 235  # faint printed box outlines

SECTIONS = {
    0: [("HL", [f"HL{i}" for i in range(1, 8)]), ("TC", [f"TC{i}" for i in range(1, 7)])],
    1: [("LE", [f"LE{i}" for i in range(1, 7)]), ("TE", [f"TE{i}" for i in range(1, 8)])],
}


def load_template():
    with open(TEMPLATE_PATH, encoding="utf-8") as f:
        data = json.load(f)
    return data["items"], data.get("section_a", {})


def template_rule_ys(page):
    """y positions (pt) of the printed full-width horizontal rules."""
    ys = set()
    for d in page.get_drawings():
        for it in d["items"]:
            if it[0] == "l":
                p1, p2 = it[1], it[2]
                if abs(p1.y - p2.y) < 0.6 and abs(p2.x - p1.x) > 100:
                    ys.add(round(p1.y, 1))
            elif it[0] == "re":
                r = it[1]
                if r.height < 1.2 and r.width > 100:
                    ys.add(round(r.y0, 1))
    return sorted(ys)


def render_gray(page):
    pix = page.get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), colorspace=fitz.csGRAY, alpha=False)
    return np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width)


def deskew_angle(ink):
    def score(arr, a):
        r = ndimage.rotate(arr, a, reshape=False, order=1, mode="constant", cval=0.0)
        p = r.mean(axis=1)
        return float(((p - p.mean()) ** 2).mean())

    coarse = ink[::4, ::4].astype(np.float32)
    best = max(np.arange(-2.5, 2.51, 0.1), key=lambda a: score(coarse, a))
    fine = ink[::2, ::2].astype(np.float32)
    return max(np.arange(best - 0.12, best + 0.121, 0.03), key=lambda a: score(fine, a))


def rotate(arr, angle):
    return ndimage.rotate(arr.astype(np.float32), angle, reshape=False,
                          order=1, mode="constant", cval=0.0)


def scan_rule_ys(ink_dark):
    prof = ink_dark[:, 150:3450].mean(axis=1)
    rows = np.where(prof > 0.6)[0]
    groups, cur = [], []
    for r in rows:
        if cur and r - cur[-1] > 3:
            groups.append(cur)
            cur = []
        cur.append(r)
    if cur:
        groups.append(cur)
    return np.array([float(np.mean(g)) / SCALE for g in groups])


def fit_y(template_ys, scan_ys):
    """Brute-force scale/offset maximising inlier count, then least-squares refine.
    Immune to spurious or missing rules, unlike an ICP-style nearest-neighbour fit."""
    tr = np.array(template_ys, dtype=float)
    if len(tr) < 5 or len(scan_ys) < 5:
        return None
    best = (-1, 1.0, 0.0)
    for s in np.arange(0.90, 1.0501, 0.002):
        for o in np.arange(-40, 60.1, 0.5):
            pred = tr * s + o
            d = np.abs(scan_ys[None, :] - pred[:, None]).min(axis=1)
            n = int((d < 1.5).sum())
            if n > best[0]:
                best = (n, s, o)
    n, s, o = best
    if n < 8:
        return None
    for _ in range(2):
        pred = tr * s + o
        idx = np.abs(scan_ys[None, :] - pred[:, None]).argmin(axis=1)
        keep = np.abs(scan_ys[idx] - pred) < 2.5
        if keep.sum() < 6:
            return None
        s, o = np.polyfit(tr[keep], scan_ys[idx][keep], 1)
    pred = tr * s + o
    idx = np.abs(scan_ys[None, :] - pred[:, None]).argmin(axis=1)
    keep = np.abs(scan_ys[idx] - pred) < 2.5
    return s, o, int(keep.sum()), float(np.abs(scan_ys[idx][keep] - pred[keep]).max())


def fit_columns(gray, template, ids, sy, oy):
    """Comb-fit the 5 checkbox columns against the faint printed outlines."""
    ys = [template[i]["row_y_pt"] for i in ids]
    y0 = max(0, int((min(ys) * sy + oy) * SCALE) - 30)
    y1 = min(gray.shape[0], int((max(ys) * sy + oy) * SCALE) + 30)
    if y1 - y0 < 40:
        return None
    prof = (gray[y0:y1, :] < STRUCT_THRESHOLD).astype(np.float32).mean(axis=0)
    L = len(prof)
    base_x = template[ids[0]]["col_x_pt"]
    best = (-1.0, None)
    for s in np.arange(sy - 0.02, sy + 0.0201, 0.002):
        for o in np.arange(-80, 221, 2):
            centres = [t * s * SCALE + o for t in base_x]
            if centres[0] < 25 or centres[-1] >= L - 25:
                continue
            weakest = min(prof[int(c) - 12:int(c) + 12].mean() for c in centres)
            if weakest > best[0]:
                best = (weakest, centres)
    return best[1]


def classify_section_a(ink_dark, options, sy, oy, sx, ox, half=16):
    """Section A options are unevenly spaced and carry labels, so the winner is the
    option box with most ink rather than a fixed 5-column argmax. The x-transform is
    reused from the Likert comb fit on the same page (scale is uniform page-wide)."""
    h, w = ink_dark.shape
    scores = []
    for opt in options:
        cx = opt["x_pt"] * sx * SCALE + ox
        cy = (opt["y_pt"] * sy + oy) * SCALE
        y0, y1 = max(0, int(cy - half)), min(h, int(cy + half))
        x0, x1 = max(0, int(cx - half)), min(w, int(cx + half))
        scores.append(float(ink_dark[y0:y1, x0:x1].mean()) if y1 > y0 and x1 > x0 else 0.0)
    if max(scores) < 0.01:
        return None, "blank_no_ink"
    base = float(np.median(scores))
    rel = [v - base for v in scores]
    order = sorted(range(len(rel)), key=lambda i: -rel[i])
    label = options[order[0]]["label"]
    weak = rel[order[0]] < 0.04
    close = len(rel) > 1 and rel[order[0]] - rel[order[1]] < 0.03
    return label, ("low_confidence" if (weak or close) else None)


def classify(ink_dark, cy, col_centres, half=18):
    h, w = ink_dark.shape
    scores = []
    for cx in col_centres:
        y0, y1 = max(0, int(cy - half)), min(h, int(cy + half))
        x0, x1 = max(0, int(cx - half)), min(w, int(cx + half))
        scores.append(float(ink_dark[y0:y1, x0:x1].mean()) if y1 > y0 and x1 > x0 else 0.0)
    # Best guess is preferred over abstaining, but a row with no ink at all is left
    # null: argmax on all-zero scores would always return column 1 and fabricate a
    # systematic bias toward "Strongly Disagree".
    if max(scores) < 0.01:
        return None, "blank_no_ink"
    base = float(np.median(scores))
    rel = [v - base for v in scores]
    order = sorted(range(5), key=lambda i: -rel[i])
    weak = rel[order[0]] < 0.04
    close = rel[order[0]] - rel[order[1]] < 0.03
    return order[0] + 1, ("low_confidence" if (weak or close) else None)


def x_transform(centres_px, template_x_pt):
    """Recover (scale_x, offset_x) from the fitted Likert column centres, so the same
    transform can be applied to Section A boxes elsewhere on the page."""
    tx = np.array(template_x_pt, dtype=float) * SCALE
    return np.polyfit(tx, np.array(centres_px, dtype=float), 1)


def process_response(scan, tmpl, template, section_a, resp_no):
    record = {
        "response_id": f"Manual-{resp_no:02d}",
        "source": "manual",
        "source_reference": {"pdf_pages": [(resp_no - 1) * 2 + 1, (resp_no - 1) * 2 + 2]},
        "answers": {},
        "flags": [],
    }

    for pidx in (0, 1):
        gray_raw = render_gray(scan[(resp_no - 1) * 2 + pidx])
        angle = deskew_angle(gray_raw < MARK_THRESHOLD)
        ink_dark = rotate(gray_raw < MARK_THRESHOLD, angle) > 0.5
        gray = 255 - rotate(255 - gray_raw.astype(np.float32), angle)

        fy = fit_y(template_rule_ys(tmpl[pidx]), scan_rule_ys(ink_dark))
        if fy is None:
            record["flags"].append(f"page{pidx + 1}:registration_failed")
            for _, ids in SECTIONS[pidx]:
                for iid in ids:
                    record["answers"][iid] = None
            continue
        sy, oy, _, _ = fy

        first_centres = None
        for sname, ids in SECTIONS[pidx]:
            centres = fit_columns(gray, template, ids, sy, oy)
            if centres is None:
                record["flags"].append(f"{sname}:column_fit_failed")
                for iid in ids:
                    record["answers"][iid] = None
                continue
            if first_centres is None:
                first_centres = (centres, template[ids[0]]["col_x_pt"])
            for iid in ids:
                cy = (template[iid]["row_y_pt"] * sy + oy) * SCALE
                val, flag = classify(ink_dark, cy, centres)
                record["answers"][iid] = val
                if flag:
                    record["flags"].append(f"{iid}:{flag}")

        # Section A (eligibility + profile) lives on page 1 only
        if pidx == 0 and section_a and first_centres is not None:
            sx, ox = x_transform(first_centres[0], first_centres[1])
            for field, options in section_a.items():
                val, flag = classify_section_a(ink_dark, options, sy, oy, sx, ox)
                record[field] = val
                if flag:
                    record["flags"].append(f"{field}:{flag}")

    return record


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--validate", nargs="*", type=int, default=None,
                    help="response numbers to print without writing files")
    args = ap.parse_args()

    template, section_a = load_template()
    scan = fitz.open(PDF_PATH)
    tmpl = fitz.open(TEMPLATE_PDF)
    n_responses = len(scan) // 2
    targets = args.validate if args.validate else list(range(1, n_responses + 1))

    OUT_DIR.mkdir(exist_ok=True)
    n_flagged = n_items = n_abstained = 0

    for resp_no in targets:
        record = process_response(scan, tmpl, template, section_a, resp_no)
        n_items += len(record["answers"])
        n_abstained += sum(1 for v in record["answers"].values() if v is None)
        if record["flags"]:
            n_flagged += 1

        if args.validate:
            print(json.dumps(record, indent=2))
            continue
        with open(OUT_DIR / f"{record['response_id']}.json", "w", encoding="utf-8") as f:
            json.dump(record, f, indent=2, ensure_ascii=False)

    if not args.validate:
        print(f"Wrote {len(targets)} files to {OUT_DIR}")
        print(f"{n_flagged} response(s) carry at least one flag")
        print(f"{n_abstained}/{n_items} items abstained "
              f"({100 * n_abstained / max(n_items, 1):.1f}%) — check these against the scan")


if __name__ == "__main__":
    main()
