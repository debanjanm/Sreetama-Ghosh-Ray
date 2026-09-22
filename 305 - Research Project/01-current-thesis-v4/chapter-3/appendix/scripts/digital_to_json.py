#!/usr/bin/env python3
"""Convert Google Form response export (.xlsx) into one JSON per respondent.

Usage:
    python3 digital_to_json.py

Reads "Hybrid Learning and Training Effectiveness at Union Bank of India (Responses).xlsx"
from the appendix folder, writes interim/Digital-NN.json (one file per row),
keyed by the item ids in questionnaire.json.
"""
import json
import re
from pathlib import Path

import openpyxl

APPENDIX = Path(__file__).resolve().parent.parent
XLSX_PATH = APPENDIX / "Hybrid Learning and Training Effectiveness at Union Bank of India (Responses).xlsx"
SCHEMA_PATH = APPENDIX / "questionnaire.json"
OUT_DIR = APPENDIX / "interim"

# Fixed column order confirmed against the schema: Timestamp, Q1..Q4, then Q5..Q30 in order.
LIKERT_ITEM_IDS = [
    "HL1", "HL2", "HL3", "HL4", "HL5", "HL6", "HL7",
    "TC1", "TC2", "TC3", "TC4", "TC5", "TC6",
    "LE1", "LE2", "LE3", "LE4", "LE5", "LE6",
    "TE1", "TE2", "TE3", "TE4", "TE5", "TE6", "TE7",
]
PROFILE_FIELDS = ["Q2_age_group", "Q3_length_of_service", "Q4_job_level"]


def parse_likert(raw):
    """'4 — Agree' -> 4. Returns None if blank/unparseable."""
    if raw is None:
        return None
    s = str(raw).strip()
    if not s:
        return None
    m = re.match(r"^\s*([1-5])\b", s)
    if not m:
        return None
    return int(m.group(1))


def main():
    with open(SCHEMA_PATH, encoding="utf-8") as f:
        schema = json.load(f)
    valid_ids = {q["id"] for section in schema["sections"] if "questions" in section
                 for q in section["questions"] if "id" in q}
    assert set(LIKERT_ITEM_IDS) <= valid_ids, "item id mismatch against questionnaire.json"

    OUT_DIR.mkdir(exist_ok=True)

    wb = openpyxl.load_workbook(XLSX_PATH, data_only=True)
    ws = wb.active
    rows = list(ws.iter_rows(values_only=True))
    header, data_rows = rows[0], rows[1:]

    n_written, n_flagged = 0, 0
    for i, row in enumerate(data_rows, start=1):
        timestamp = row[0]
        eligibility = row[1]
        record = {
            "response_id": f"Digital-{i:02d}",
            "source": "digital",
            "source_reference": {"sheet_row": i + 1, "timestamp": str(timestamp) if timestamp else None},
            "Q1_eligibility": eligibility,
            "flags": [],
        }

        eligible = str(eligibility).strip().lower() == "yes"
        if not eligible:
            record["flags"].append("ineligible_or_blank_Q1")

        for j, field in enumerate(PROFILE_FIELDS, start=2):
            record[field] = row[j]

        answers = {}
        for k, item_id in enumerate(LIKERT_ITEM_IDS, start=5):
            val = parse_likert(row[k])
            answers[item_id] = val
            if eligible and val is None:
                record["flags"].append(f"missing_{item_id}")
        record["answers"] = answers

        out_path = OUT_DIR / f"{record['response_id']}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(record, f, indent=2, ensure_ascii=False)
        n_written += 1
        if record["flags"]:
            n_flagged += 1

    print(f"Wrote {n_written} files to {OUT_DIR}")
    print(f"{n_flagged} response(s) flagged (ineligible or missing items) — review before analysis.")


if __name__ == "__main__":
    main()
