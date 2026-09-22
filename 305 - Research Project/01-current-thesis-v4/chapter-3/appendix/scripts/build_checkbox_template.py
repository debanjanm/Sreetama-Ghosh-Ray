#!/usr/bin/env python3
"""One-off: extract exact checkbox (x,y) positions in PDF points from the vector
"questionnaire-print-ready-landscape.pdf" template (the file the paper form was
printed from), and save them as checkbox_template.json for manual_to_json.py to use.

Run once; re-run only if the print-ready template layout changes.
"""
import json
from pathlib import Path

import fitz

APPENDIX = Path(__file__).resolve().parent.parent
TEMPLATE_PDF = APPENDIX / "questionnaire-print-ready-landscape.pdf"
OUT_PATH = Path(__file__).resolve().parent / "checkbox_template.json"

PAGE0_ITEM_IDS = ["HL1", "HL2", "HL3", "HL4", "HL5", "HL6", "HL7",
                  "TC1", "TC2", "TC3", "TC4", "TC5", "TC6"]
PAGE1_ITEM_IDS = ["LE1", "LE2", "LE3", "LE4", "LE5", "LE6",
                  "TE1", "TE2", "TE3", "TE4", "TE5", "TE6", "TE7"]


def extract_page_boxes(page):
    """Return list of (x_center, y_center) for every '□' glyph on the page,
    grouped into rows of 5 sorted by y then x within row."""
    d = page.get_text("dict")
    glyphs = []
    for block in d["blocks"]:
        for line in block.get("lines", []):
            for span in line["spans"]:
                if span["text"].strip() == "□":  # □
                    x0, y0, x1, y1 = span["bbox"]
                    glyphs.append(((x0 + x1) / 2, (y0 + y1) / 2))
    glyphs.sort(key=lambda p: p[1])
    rows = []
    current = []
    last_y = None
    for x, y in glyphs:
        if last_y is not None and abs(y - last_y) > 8:
            rows.append(sorted(current, key=lambda p: p[0]))
            current = []
        current.append((x, y))
        last_y = y
    if current:
        rows.append(sorted(current, key=lambda p: p[0]))
    return rows


def extract_section_a(page):
    """Section A's checkboxes sit inline with their labels, so they are not standalone
    '□' spans like the Likert grid — their positions come from char-level boxes instead.
    Each option's label is taken from the text following its box."""
    fields = {
        "Q1_eligibility": ("Yes", "No"),
        "Q2_age_group": ("Below 25", "25-34", "35-44", "45-54", "55 and above"),
        "Q3_length_of_service": ("Below 5 years", "5-10 years", "11-20 years", "Above 20 years"),
        "Q4_job_level": ("Clerical", "Officer", "Managerial", "Other"),
    }
    runs = []
    for block in page.get_text("rawdict")["blocks"]:
        for line in block.get("lines", []):
            for span in line["spans"]:
                chars = span.get("chars", [])
                if span["bbox"][1] > 200:
                    continue
                boxes = [((c["bbox"][0] + c["bbox"][2]) / 2, (c["bbox"][1] + c["bbox"][3]) / 2)
                         for c in chars if c["c"] == "□"]
                if boxes:
                    runs.append({"y": span["bbox"][1], "x0": span["bbox"][0], "boxes": boxes})

    # eligibility is the only run on the far left; the rest are ordered by y then x
    elig = [r for r in runs if r["x0"] < 100]
    others = sorted([r for r in runs if r["x0"] >= 100], key=lambda r: (r["x0"], r["y"]))

    out = {}
    if elig:
        out["Q1_eligibility"] = [
            {"label": lab, "x_pt": p[0], "y_pt": p[1]}
            for lab, p in zip(fields["Q1_eligibility"], elig[0]["boxes"])
        ]
    age = [r for r in others if len(r["boxes"]) == 5]
    if age:
        out["Q2_age_group"] = [
            {"label": lab, "x_pt": p[0], "y_pt": p[1]}
            for lab, p in zip(fields["Q2_age_group"], age[0]["boxes"])
        ]
    # length of service wraps onto a second line ("Above 20 years")
    service = [r for r in others if r["x0"] > 600 and r["y"] < 160]
    svc_boxes = [b for r in sorted(service, key=lambda r: r["y"]) for b in r["boxes"]]
    if len(svc_boxes) == 4:
        out["Q3_length_of_service"] = [
            {"label": lab, "x_pt": p[0], "y_pt": p[1]}
            for lab, p in zip(fields["Q3_length_of_service"], svc_boxes)
        ]
    job = [r for r in others if r["x0"] > 600 and r["y"] > 160]
    if job and len(job[0]["boxes"]) == 4:
        out["Q4_job_level"] = [
            {"label": lab, "x_pt": p[0], "y_pt": p[1]}
            for lab, p in zip(fields["Q4_job_level"], job[0]["boxes"])
        ]
    return out


def main():
    doc = fitz.open(TEMPLATE_PDF)
    template = {}
    for page_idx, item_ids in ((0, PAGE0_ITEM_IDS), (1, PAGE1_ITEM_IDS)):
        rows = extract_page_boxes(doc[page_idx])
        assert len(rows) == len(item_ids), (
            f"page {page_idx}: found {len(rows)} rows, expected {len(item_ids)}"
        )
        for item_id, row in zip(item_ids, rows):
            assert len(row) == 5, f"{item_id}: found {len(row)} checkboxes, expected 5"
            xs = [p[0] for p in row]
            ys = [p[1] for p in row]
            template[item_id] = {
                "page": page_idx,
                "col_x_pt": xs,
                "row_y_pt": sum(ys) / len(ys),
            }

    section_a = extract_section_a(doc[0])

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump({"page_size_pt": [doc[0].rect.width, doc[0].rect.height],
                    "items": template, "section_a": section_a}, f, indent=2)
    print(f"Wrote template for {len(template)} Likert items to {OUT_PATH}")
    for k, v in section_a.items():
        print(f"  {k}: {len(v)} options -> {[o['label'] for o in v]}")


if __name__ == "__main__":
    main()
