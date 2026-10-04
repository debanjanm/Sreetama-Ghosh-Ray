"""Reproduce the 102-case supplementary tables and code-drawn thesis figures.

The SPSS regression is not recalculated here. These supplementary tests use the
profile-complete scored CSV with Digital-01 omitted, as specified for V5.
Requires numpy and scipy; the figures use only the Python standard library.
"""

from __future__ import annotations

import csv
import json
from collections import Counter
from html import escape
from pathlib import Path

import numpy as np
from scipy import stats


ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / "03-scored-dataset/final-analysis-data.csv"
OUT = Path(__file__).resolve().parent / "outputs/v5-profile-summary"
FIGURES = ROOT.parent / "06-thesis-drafts/03-third-draft-chapters-1-to-5/figures"

rows = [row for row in csv.DictReader(CSV.open(newline="")) if row["response_id"] != "Digital-01"]
assert len(rows) == 102
assert Counter(row["source"] for row in rows) == {"manual": 54, "digital": 48}
assert all(row[k] for row in rows for k in ("age_group", "service_length", "job_level"))

constructs = {
    "Hybrid Learning": "Hybrid_Learning",
    "Trainer Competence": "Trainer_Competence",
    "Learner Engagement": "Learner_Engagement",
    "Training Effectiveness": "Training_Effectiveness",
}


def values(column: str, group: str | None = None) -> np.ndarray:
    return np.array([float(row[column]) for row in rows if group is None or row["job_level"] == group])


results: dict = {"n": 102, "source_mode": dict(Counter(row["source"] for row in rows))}
results["profile"] = {
    "age": dict(Counter(row["age_group"] for row in rows)),
    "service": dict(Counter(row["service_length"] for row in rows)),
    "level": dict(Counter(row["job_level"] for row in rows)),
}
results["one_sample_midpoint_3"] = {}
for label, column in constructs.items():
    x = values(column)
    test = stats.ttest_1samp(x, 3)
    results["one_sample_midpoint_3"][label] = {
        "mean": float(x.mean()), "t": float(test.statistic), "df": 101, "p": float(test.pvalue)
    }

officer = values("Training_Effectiveness", "Officer")
managerial = values("Training_Effectiveness", "Managerial")
welch = stats.ttest_ind(officer, managerial, equal_var=False)
results["officer_managerial_te_welch"] = {
    "n_officer": len(officer), "n_managerial": len(managerial),
    "mean_officer": float(officer.mean()), "mean_managerial": float(managerial.mean()),
    "t": float(welch.statistic), "df": float(welch.df), "p": float(welch.pvalue),
}

results["paired_with_te"] = {}
te = values("Training_Effectiveness")
for label, column in list(constructs.items())[:3]:
    x = values(column)
    test = stats.ttest_rel(x, te)
    results["paired_with_te"][label] = {
        "mean_difference": float((x - te).mean()), "t": float(test.statistic),
        "df": 101, "p": float(test.pvalue),
    }

levels = [values("Training_Effectiveness", group) for group in ("Clerical", "Officer", "Managerial")]
anova = stats.f_oneway(*levels)
results["te_by_job_level_anova"] = {
    "group_means": {group: float(x.mean()) for group, x in zip(("Clerical", "Officer", "Managerial"), levels)},
    "F": float(anova.statistic), "df_between": 2, "df_within": 99, "p": float(anova.pvalue),
}

results["raw_mean_crosstabs"] = {}
for label, column in list(constructs.items())[:3]:
    x = [round(float(row[column]), 6) for row in rows]
    y = [round(float(row["Training_Effectiveness"]), 6) for row in rows]
    ux, uy = sorted(set(x)), sorted(set(y))
    matrix = np.array([[sum(a == xx and b == yy for a, b in zip(x, y)) for yy in uy] for xx in ux])
    chi = stats.chi2_contingency(matrix, correction=False)
    results["raw_mean_crosstabs"][label] = {
        "shape": list(matrix.shape), "chi_square": float(chi.statistic), "df": int(chi.dof),
        "p": float(chi.pvalue), "expected_below_5_percent": float((chi.expected_freq < 5).mean() * 100),
        "minimum_expected": float(chi.expected_freq.min()),
        "interpretation": "Invalid for inference because nearly all expected cell counts are below five.",
    }

item_groups = {
    "Hybrid Learning": [(f"HL{i}", i + 4) for i in range(1, 8)],
    "Trainer Competence": [(f"TC{i}", i + 11) for i in range(1, 7)],
    "Learner Engagement": [(f"LE{i}", i + 17) for i in range(1, 7)],
    "Training Effectiveness": [(f"TE{i}", i + 23) for i in range(1, 8)],
}
item_counts = {}
for group, items in item_groups.items():
    for code, number in items:
        counts = Counter(int(row[code]) for row in rows)
        assert all(1 <= int(row[code]) <= 5 for row in rows)
        assert sum(counts.values()) == 102
        item_counts[f"Q{number}"] = {str(i): counts[i] for i in range(1, 6)}
results["item_frequencies"] = item_counts

OUT.mkdir(parents=True, exist_ok=True)
FIGURES.mkdir(parents=True, exist_ok=True)
(OUT / "supplementary-tests-102.json").write_text(json.dumps(results, indent=2) + "\n")


def bar_svg(path: Path, title: str, labels: list[str], numbers: list[float], *, maximum: float,
            unit: str, baseline: float = 0, color: str = "#245a81") -> None:
    width = 900
    left, right, top, row_height = 245, 75, 105, 62
    height = top + len(labels) * row_height + 55
    plot = width - left - right
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title)}">',
        f'<rect width="{width}" height="{height}" fill="white"/>',
        f'<text x="30" y="42" font-family="Arial" font-size="25" font-weight="bold" fill="#172c3d">{escape(title)}</text>',
        f'<text x="30" y="69" font-family="Arial" font-size="15" fill="#486171">{escape(unit)}</text>',
    ]
    for i, (label, number) in enumerate(zip(labels, numbers)):
        y = top + i * row_height
        value_width = max(0, plot * number / maximum)
        parts += [
            f'<text x="30" y="{y+27}" font-family="Arial" font-size="17" fill="#172c3d">{escape(label)}</text>',
            f'<rect x="{left}" y="{y}" width="{plot}" height="37" fill="#eef2f5" rx="5"/>',
            f'<rect x="{left}" y="{y}" width="{value_width:.1f}" height="37" fill="{color}" rx="5"/>',
            f'<text x="{left+value_width+9:.1f}" y="{y+26}" font-family="Arial" font-size="16" font-weight="bold" fill="#172c3d">{number:.3f}</text>' if unit.startswith("Mean") else
            f'<text x="{left+value_width+9:.1f}" y="{y+26}" font-family="Arial" font-size="16" font-weight="bold" fill="#172c3d">{int(number)}</text>',
        ]
    if baseline:
        bx = left + plot * baseline / maximum
        parts += [f'<line x1="{bx:.1f}" y1="88" x2="{bx:.1f}" y2="{height-34}" stroke="#a54a3d" stroke-width="2" stroke-dasharray="6,5"/>',
                  f'<text x="{bx+5:.1f}" y="98" font-family="Arial" font-size="13" fill="#a54a3d">neutral = {baseline:g}</text>']
    parts.append('</svg>')
    path.write_text("\n".join(parts) + "\n")


age_labels = ["Below 25", "25–34", "35–44", "45–54", "55 and above"]
age_counts = [results["profile"]["age"].get(x, 0) for x in ["Below 25", "25–34", "35–44", "45–54", "55 and above"]]
bar_svg(FIGURES / "figure-4-1-age.svg", "Respondents by age group", age_labels, age_counts,
        maximum=60, unit="Number of respondents; N = 102")
service_labels = ["Below 5 years", "5–10 years", "11–20 years", "Above 20 years"]
bar_svg(FIGURES / "figure-4-2-service.svg", "Respondents by length of service", service_labels,
        [results["profile"]["service"].get(x, 0) for x in service_labels], maximum=60,
        unit="Number of respondents; N = 102")
level_labels = ["Clerical", "Officer", "Managerial"]
bar_svg(FIGURES / "figure-4-3-level.svg", "Respondents by job level", level_labels,
        [results["profile"]["level"].get(x, 0) for x in level_labels], maximum=60,
        unit="Number of respondents; N = 102")
bar_svg(FIGURES / "figure-4-4-construct-means.svg", "Construct means from SPSS Explore", list(constructs),
        [4.148, 4.158, 4.317, 4.254], maximum=5, unit="Mean response on a five-point scale; valid N = 102",
        baseline=3, color="#397d75")


def stacked_svg(path: Path, title: str, question_numbers: list[int]) -> None:
    width, left, top, bar_width, row_height = 900, 125, 105, 660, 60
    height = top + len(question_numbers) * row_height + 82
    colors = ["#b95d58", "#db9b74", "#d3d9dc", "#74a9a4", "#2d766e"]
    labels = ["1 Strongly disagree", "2 Disagree", "3 Neutral", "4 Agree", "5 Strongly agree"]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title)}">',
        f'<rect width="{width}" height="{height}" fill="white"/>',
        f'<text x="28" y="40" font-family="Arial" font-size="24" font-weight="bold" fill="#172c3d">{escape(title)}</text>',
        '<text x="28" y="68" font-family="Arial" font-size="15" fill="#486171">Percent of 102 respondents in each response category</text>',
    ]
    for j, q in enumerate(question_numbers):
        y = top + j * row_height
        parts.append(f'<text x="35" y="{y+27}" font-family="Arial" font-size="17" fill="#172c3d">Q{q}</text>')
        x = left
        for score in range(1, 6):
            count = item_counts[f"Q{q}"][str(score)]
            w = bar_width * count / 102
            if w:
                parts.append(f'<rect x="{x:.2f}" y="{y}" width="{w:.2f}" height="38" fill="{colors[score-1]}"/>')
                if w > 35:
                    parts.append(f'<text x="{x+w/2:.2f}" y="{y+25}" text-anchor="middle" font-family="Arial" font-size="14" font-weight="bold" fill="white">{count}</text>')
            x += w
    lx = 40
    ly = height - 38
    for label, color in zip(labels, colors):
        parts.append(f'<rect x="{lx}" y="{ly-12}" width="13" height="13" fill="{color}"/>')
        parts.append(f'<text x="{lx+18}" y="{ly}" font-family="Arial" font-size="12" fill="#172c3d">{escape(label)}</text>')
        lx += 165
    parts.append('</svg>')
    path.write_text("\n".join(parts) + "\n")


for i, (group, items) in enumerate(item_groups.items(), start=5):
    stacked_svg(FIGURES / f"figure-4-{i}-{group.lower().replace(' ', '-')}.svg", group + " item responses",
                [number for _, number in items])
