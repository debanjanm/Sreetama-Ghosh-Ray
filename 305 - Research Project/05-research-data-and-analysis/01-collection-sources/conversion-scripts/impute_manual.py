#!/usr/bin/env python3
"""Apply the imputation/exclusion rule already written into Chapter 3, section 3.6,
to the manually-verified Manual-*.json files, writing the result to ../imputed/.

Rule (verbatim from chapter-3-research-methodology.md):
    "Question 1 screens for eligibility. Only responses marked 'Yes' are included
    in the final analysis. Responses marked 'No' or with a blank eligibility answer
    are excluded... When an otherwise eligible response has one blank or unclear
    Likert item, that item is replaced with the respondent's arithmetic mean for
    the remaining items of the same construct and the imputation is recorded.
    Responses with two or more blank or unclear scored items are excluded."

This script does not decide policy - it applies the policy already committed to
in the thesis text. If that text changes, update this script to match, not the
other way round.

Usage:
    python3 impute_manual.py
"""
import json
from pathlib import Path

APPENDIX = Path(__file__).resolve().parent.parent
SRC_DIR = APPENDIX / "interim"
OUT_DIR = APPENDIX / "imputed"

CONSTRUCTS = {
    "HL": [f"HL{i}" for i in range(1, 8)],
    "TC": [f"TC{i}" for i in range(1, 7)],
    "LE": [f"LE{i}" for i in range(1, 7)],
    "TE": [f"TE{i}" for i in range(1, 8)],
}
ITEM_TO_CONSTRUCT = {item: c for c, items in CONSTRUCTS.items() for item in items}


def process(record):
    out = dict(record)
    answers = dict(record["answers"])
    eligibility = str(record.get("Q1_eligibility") or "").strip().lower()

    if eligibility != "yes":
        out["status"] = "excluded"
        out["exclusion_reason"] = "ineligible_or_blank_eligibility"
        out["imputations"] = []
        return out

    null_items = [k for k, v in answers.items() if v is None]

    if len(null_items) == 0:
        out["status"] = "retained"
        out["exclusion_reason"] = None
        out["imputations"] = []
        return out

    if len(null_items) >= 2:
        out["status"] = "excluded"
        out["exclusion_reason"] = f"two_or_more_missing_items ({len(null_items)})"
        out["imputations"] = []
        return out

    # exactly one missing item: mean-impute from the rest of its own construct
    item = null_items[0]
    construct = ITEM_TO_CONSTRUCT[item]
    peers = [answers[i] for i in CONSTRUCTS[construct] if i != item and answers[i] is not None]
    if not peers:
        out["status"] = "excluded"
        out["exclusion_reason"] = "construct_fully_missing"
        out["imputations"] = []
        return out

    mean_value = sum(peers) / len(peers)
    answers[item] = round(mean_value, 3)
    out["answers"] = answers
    out["status"] = "retained_with_imputation"
    out["exclusion_reason"] = None
    out["imputations"] = [{
        "item": item,
        "construct": construct,
        "imputed_value": answers[item],
        "method": "construct_mean_of_remaining_items",
        "peers_used": len(peers),
    }]
    return out


def main():
    OUT_DIR.mkdir(exist_ok=True)
    counts = {"retained": 0, "retained_with_imputation": 0, "excluded": 0}
    for f in sorted(SRC_DIR.glob("Manual-*.json"), key=lambda p: int(p.stem.split("-")[1])):
        record = json.load(open(f, encoding="utf-8"))
        result = process(record)
        counts[result["status"]] += 1
        with open(OUT_DIR / f.name, "w", encoding="utf-8") as fh:
            json.dump(result, fh, indent=2, ensure_ascii=False)

    print(f"Wrote {sum(counts.values())} files to {OUT_DIR}")
    for k, v in counts.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
