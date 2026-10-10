"""Merge the pasted paraphrased chunks back into the revision draft -> ../../earlier-source-versions/third-draft-source-paraphrased.md
Only chapter prose is replaced; tables, captions, figures, References and appendices stay as in the revision.
All 13 chunks are merged (chunk 02 was re-pasted with line breaks).
"""
import re, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..", "..", "earlier-source-versions")
rev = open(os.path.join(ROOT, "third-draft-source-prose-revision.md"), encoding="utf8").read().split("\n")
COUNTS = [21,30,23,21,22,27,34,23,31,30,28,28,3]
SKIP_CHUNKS = set()

# 1) units, same rules as make_chunks_1000.py
units, chap, code, para, ps = [], None, False, [], 0
def flush(n):
    global para
    if para: units.append(("p", list(para), ps, n - 1)); para = []
for n, line in enumerate(rev, 1):
    if line.startswith("```"): flush(n); code = not code; continue
    if code: continue
    s = line.rstrip()
    if s.startswith("# "):
        flush(n); chap = s[2:] if s[2:].startswith("Chapter") else None
        if chap: units.append(("h", [s], n, n))
        continue
    if chap is None: continue
    if s.startswith("#"): flush(n); units.append(("h", [s], n, n)); continue
    if not s.strip() or s.startswith(("|","!",">","    ")) or re.match(r"\*\*(Table|Figure) ", s) or s.startswith("*Source") or s.strip() == "---": flush(n); continue
    if not para: ps = n
    para.append(s)
flush(len(rev) + 1)
assert len(units) == sum(COUNTS), (len(units), sum(COUNTS))

# 2) paraphrased blocks per chunk
blocks = {}
for i, c in enumerate(COUNTS, 1):
    lines = [l.strip() for l in open(os.path.join(HERE, f"chunk-{i:02d}.txt"), encoding="utf8").read().split("\n") if l.strip()]
    blocks[i] = lines if (len(lines) == c and i not in SKIP_CHUNKS) else None

# 3) mechanical, meaning-preserving fixes (each is logged)
log = {}
def sub(rx, rep, t, tag, flags=0):
    new, n = re.subn(rx, rep, t, flags=flags)
    if n: log[tag] = log.get(tag, 0) + n
    return new
CONTR = {"don't":"do not","doesn't":"does not","isn't":"is not","aren't":"are not","wasn't":"was not","weren't":"were not","won't":"will not","can't":"cannot","couldn't":"could not","shouldn't":"should not","wouldn't":"would not","hasn't":"has not","haven't":"have not","didn't":"did not","it's":"it is","that's":"that is","there's":"there is"}
UK = [("programs","programmes"),("program","programme"),("Programs","Programmes"),("Program","Programme"),("organizational","organisational"),("organizations","organisations"),("organization","organisation"),("utilizes","utilises"),("utilized","utilised"),("utilizing","utilising"),("utilize","utilise"),("behaviors","behaviours"),("behavior","behaviour"),("recognizes","recognises"),("recognized","recognised"),("recognize","recognise"),("emphasizes","emphasises"),("emphasized","emphasised"),("emphasize","emphasise"),("favorable","favourable"),("centers","centres"),("center","centre"),("analyze","analyse"),("summarize","summarise"),("labor","labour"),("characterize","characterise"),("organized","organised"),("organizing","organising"),("organize","organise"),("specialized","specialised"),("personalized","personalised"),("generalized","generalised"),("nationalized","nationalised"),("realized","realised"),("practicing","practising")]
SPECIFIC = [
 ("Mulaudzi (2011)", "Mulaudzi (2021)"),
 ("Training, evaluation, and transfer literature supports", "Training-evaluation and transfer literature supports"),
 ("phased programs", "staggered programmes"),
 ("the chances for students to participate actively", "opportunities to participate actively"),
 ("The study examines if the evaluation of Hybrid Learning, Trainer Competence, and Learner Engagement together influence the perception of Training Effectiveness.", "The study examines whether ratings of Hybrid Learning, Trainer Competence, and Learner Engagement jointly relate to perceived Training Effectiveness."),
 ("The design is not capable of accounting for later changes in work behavior or bank performance that may result from training.", "The design cannot show whether training caused later changes in work behaviour or Bank performance."),
 ("Sosnova and her colleagues in 2025 investigate", "Sosnova et al. (2025) investigate"),
 ("stay open for future editing", "remain available for later revision"),
 ("stayed available for editing", "stayed available for revision"),
 ("the research assumption", "the hypothesis"),
 ("The general assumption that there is no relationship between the predictors and perceived Training Effectiveness is rejected", "The null hypothesis, that the predictors have no joint relationship with perceived Training Effectiveness, is rejected"),
 (", which is part of Union Bank of India as stated in the 2025 report", " (Union Bank of India, 2025)"),
 ("The model is significant, with an F-value of 50.652 and a p-value less than .001.", "The model is significant, F(3, 98) = 50.652, p < .001."),
 ("with an F-value of 1.629 and a p-value of 0.201", "F(2, 99) = 1.629, p = .201"),
 ("with a t-value of −0.270 and a p-value of .788", "t(52.261) = −0.270, p = .788"),
 ("Normality tests are important for all four construct means, which aligns with the presence of skewed distributions.", "Normality tests in the Explore output are statistically significant for all four construct means, consistent with the negatively skewed ratings."),
 ("The null hypothesis is not supported, and the alternative hypothesis is accepted based on the combined model.", "The null hypothesis is rejected, and the alternative hypothesis is supported for the combined model."),
 ("R squared value of 0.608", "R² of .608"),
 ("together influence Training Effectiveness", "jointly predict Training Effectiveness"),
 ("together influence the effectiveness of training", "jointly predict Training Effectiveness"),
 ("three separate factors that influence the perception of Training Effectiveness", "three separate predictors of perceived Training Effectiveness"),
 ("One of the key tools used by the Bank for reporting is Union Vidya, its Learning Management System (LMS).In addition to this, the Bank utilizes a variety of learning resources such as e-books, podcasts, audiobooks, microlearning content, virtual workshops, role-based learning programs, mandatory e-learning for officers, and a Training Management System.", "The Bank’s annual reports describe Union Vidya, its Learning Management System (LMS), together with learning resources such as e-books, podcasts, audiobooks, microlearning content, virtual workshops, role-based learning programmes, mandatory e-learning for officers, and a Training Management System (Union Bank of India, 2024, 2025)."),
 ("In 2017, Vo, Zhu, and Diep combined", "Vo, Zhu and Diep (2017) combined"),
 ("In 2026, Uddin, Ahamed, Jakowan, Islam, and Nahar conducted", "Uddin, Ahamed, Jakowan, Islam and Nahar (2026) conducted"),
 ("Their correlations with each other stay positive, including a strong link between them.", "The two are also strongly and positively correlated with each other (Table 4.6)."),
]
def fix(t):
    for a, b in SPECIFIC:
        if a in t: log["specific: " + a[:50]] = log.get("specific: " + a[:50], 0) + t.count(a); t = t.replace(a, b)
    for k, v in CONTR.items():
        t = sub(r"\b" + k + r"\b", v, t, "contractions expanded", re.I) if True else t
    t = sub(r"\bcan not\b", "cannot", t, "contractions expanded")
    for a, b in UK: t = sub(r"\b" + a + r"\b", b, t, "US to UK spelling")
    t = sub(r"al\.\(", "al. (", t, "space after et al.")
    t = sub(r"al\.(?=[a-z])", "al. ", t, "space after et al.")
    t = sub(r"(?<=[a-z\)])\.(?=[A-Z][a-z])", ". ", t, "missing space after full stop")
    t = sub(r"(?<=[a-z\)])\?(?=[A-Z][a-z])", "? ", t, "missing space after question mark")
    t = sub(r"(?<=[a-z]), and (?=[A-Z][a-z]+(?:[’']s)? \(\d{4})", " and ", t, "serial comma removed in author lists")
    t = sub(r"(?<=\w)'(?=\w)", "’", t, "straight to curly apostrophes")
    t = sub(r"(?<=s)'(?=\s)", "’", t, "straight to curly apostrophes")
    t = sub(r"R squared", "R²", t, "R squared to R²")
    return t

def split_items(text, n):
    text = re.sub(r"(?<!\d)\d\.\s*", "", text.strip())
    parts = [p.strip() for p in re.split(r"(?<=[.?!;])\s*(?=[A-Z])", text) if p.strip()]
    return parts if len(parts) == n else None

out = list(rev); k = 0; notes = {"headings_changed": [], "lists_kept": [], "replaced": 0, "kept": 0}
plan = []
for ci, c in enumerate(COUNTS, 1):
    for j in range(c):
        kind, lines_, a, b = units[k]; k += 1
        newb = blocks[ci][j] if blocks[ci] else None
        plan.append((kind, lines_, a, b, newb, ci))
for kind, lines_, a, b, newb, ci in reversed(plan):
    if newb is None: notes["kept"] += 1; continue
    if kind == "h":
        orig = re.sub(r"^#+\s*", "", lines_[0]).strip()
        if re.sub(r"[^a-z0-9]", "", orig.lower()) != re.sub(r"[^a-z0-9]", "", newb.lower()): notes["headings_changed"].append((ci, orig, newb))
        continue
    if len(lines_) > 1:  # list
        items = split_items(fix(newb), len(lines_))
        if not items: notes["lists_kept"].append((ci, lines_[0][:50])); continue
        marker_num = bool(re.match(r"\d+\.", lines_[0]))
        out[a-1:b] = [(f"{i}. " if marker_num else "- ") + t for i, t in enumerate(items, 1)]
        notes["replaced"] += 1; continue
    out[a-1:b] = [fix(newb)]; notes["replaced"] += 1
open(os.path.join(ROOT, "third-draft-source-paraphrased.md"), "w", encoding="utf8").write("\n".join(out))
json.dump({"log": log, "notes": notes}, open(os.path.join(HERE, "_merge_log.json"), "w"), ensure_ascii=False, indent=1)
print(log); print({k: (v if not isinstance(v, list) else len(v)) for k, v in notes.items()}); print(notes["headings_changed"][:6]); print(notes["lists_kept"])
