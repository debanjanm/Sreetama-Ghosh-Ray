"""Split the prose of third-draft-source-prose-revision.md into chunks of at most 5,000 words.

Keeps headings, paragraphs and lists exactly as written in the .md (so edited text can be pasted straight back).
Leaves out tables, captions, figures, 'Source:' lines, code blocks, References and the appendices.
Run:  python3 make_humanize_chunks.py
"""
import re, os, glob
LIMIT = 5000
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "..", "earlier-source-versions", "third-draft-source-prose-revision.md")

units = []  # (kind, text, first_line, last_line) ; kind: h1/h2/h3/p
cur_chap = None; code = False; para = []; pstart = 0
def flush(n):
    global para
    if para: units.append(("p", "\n".join(para), pstart, n - 1)); para = []
lines = open(SRC, encoding="utf8").read().split("\n")
for n, line in enumerate(lines, 1):
    if line.startswith("```"): flush(n); code = not code; continue
    if code: continue
    s = line.rstrip()
    if s.startswith("# "):
        flush(n); h = s[2:]
        cur_chap = h if h.startswith("Chapter") else None
        if cur_chap: units.append(("h1", s, n, n))
        continue
    if cur_chap is None: continue
    if s.startswith("#"):
        flush(n); units.append(("h2" if s.startswith("## ") else "h3", s, n, n)); continue
    skip = (s.startswith(("|", "!", ">")) or re.match(r"\*\*(Table|Figure) ", s) or s.startswith("*Source") or s.strip() == "---" or s.startswith("    "))
    if not s.strip() or skip:
        flush(n); continue
    if not para: pstart = n
    para.append(s)
flush(len(lines) + 1)

words = lambda t: len(re.sub(r"[#*`]", "", t).split())
chunks, cur, cw = [], [], 0
def close():
    global cur, cw
    if cur: chunks.append(cur); cur, cw = [], 0
i = 0
while i < len(units):
    k, t, a, b = units[i]
    # at a chapter/section heading, look ahead: would the whole section fit?
    if k in ("h1", "h2"):
        j = i + 1; sw = 0
        while j < len(units) and units[j][0] not in ("h1", "h2"): sw += words(units[j][1]) if units[j][0] == "p" else 0; j += 1
        if cur and cw + sw > LIMIT: close()
    w = words(t) if k == "p" else 0
    if cur and cw + w > LIMIT: close()
    cur.append(units[i]); cw += w; i += 1
close()

for f in glob.glob(os.path.join(HERE, "chunk-*.md")): os.remove(f)
rows = []
for n, ch in enumerate(chunks, 1):
    text = "\n\n".join(u[1] for u in ch) + "\n"
    heads = [u[1].lstrip("# ") for u in ch if u[0] in ("h1", "h2", "h3")]
    name = f"chunk-{n}-of-{len(chunks)}.md"
    open(os.path.join(HERE, name), "w", encoding="utf8").write(text)
    rows.append((name, sum(words(u[1]) for u in ch if u[0] == "p"), len(text), heads[0], heads[-1], ch[0][2], ch[-1][3]))
with open(os.path.join(HERE, "chunk-index.md"), "w", encoding="utf8") as f:
    f.write("# Humanise chunks (max 5,000 words each)\n\nSource: `../third-draft-source-prose-revision.md`. Tables, captions, figures, References and appendices are not included.\nEdit one chunk at a time, then paste the revised paragraphs back at the line range shown.\n\n")
    f.write("| Chunk | Words | Characters | Starts at | Ends at | Source lines |\n| --- | ---: | ---: | --- | --- | --- |\n")
    for r in rows: f.write(f"| {r[0]} | {r[1]:,} | {r[2]:,} | {r[3]} | {r[4]} | {r[5]}–{r[6]} |\n")
    f.write(f"| **Total** | **{sum(r[1] for r in rows):,}** | | | | |\n")
print([(r[0], r[1]) for r in rows])
