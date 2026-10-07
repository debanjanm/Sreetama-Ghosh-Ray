"""Split the prose of third-draft-source-prose-revision.md into plain-text chunks of at most 950 words
(the AI-detection site accepts 1,000 words per check). Tables, captions, figures, 'Source:' lines,
code blocks, References and appendices are left out. Run: python3 make_chunks_1000.py
"""
import re, os, glob
LIMIT = 950
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "third-draft-source-prose-revision.md")

def clean(t):
    t = re.sub(r"`([^`]*)`", r"\1", t); t = re.sub(r"\*\*([^*]+)\*\*", r"\1", t)
    return re.sub(r"\*([^*\s][^*]*)\*", r"\1", t).strip()

units, chap, code, para, ps = [], None, False, [], 0   # (kind, text, first_line, last_line)
def flush(n):
    global para
    if para: units.append(("p", clean(" ".join(para)), ps, n - 1)); para = []
lines = open(SRC, encoding="utf8").read().split("\n")
for n, line in enumerate(lines, 1):
    if line.startswith("```"): flush(n); code = not code; continue
    if code: continue
    s = line.rstrip()
    if s.startswith("# "):
        flush(n); chap = s[2:] if s[2:].startswith("Chapter") else None
        if chap: units.append(("h", clean(s[2:]).upper(), n, n))
        continue
    if chap is None: continue
    if s.startswith("#"): flush(n); units.append(("h", clean(s.lstrip("# ")), n, n)); continue
    if not s.strip() or s.startswith(("|", "!", ">", "    ")) or re.match(r"\*\*(Table|Figure) ", s) or s.startswith("*Source") or s.strip() == "---":
        flush(n); continue
    if not para: ps = n
    para.append(s)
flush(len(lines) + 1)

wc = lambda t: len(t.split())
# attach headings to the paragraph that follows
blocks, pend = [], []
for k, t, a, b in units:
    if k == "h": pend.append((t, a, b))
    else:
        blocks.append((pend + [(t, a, b)], t)); pend = []
chunks, cur, cw = [], [], 0
for items, ptxt in blocks:
    w = sum(wc(x[0]) for x in items)
    if cur and cw + w > LIMIT: chunks.append(cur); cur, cw = [], 0
    cur.extend(items); cw += w
if cur: chunks.append(cur)

for f in glob.glob(os.path.join(HERE, "chunk-*.txt")): os.remove(f)
rows = []
for i, ch in enumerate(chunks, 1):
    text = "\n\n".join(x[0] for x in ch) + "\n"
    name = f"chunk-{i:02d}.txt"; open(os.path.join(HERE, name), "w", encoding="utf8").write(text)
    first = next((x[0] for x in ch if x[0].isupper() or len(x[0].split()) < 12), ch[0][0][:60])
    rows.append((name, wc(text), len(text), ch[0][1], ch[-1][2]))
with open(os.path.join(HERE, "chunk-index.md"), "w", encoding="utf8") as f:
    f.write("# 1,000-word chunks (plain text, max 950 words each)\n\nSource: `../third-draft-source-prose-revision.md`. Tables, captions, figures, References and appendices are not included. Paste edits back at the line range shown.\n\n")
    f.write("| Chunk | Words | Characters | Source lines |\n| --- | ---: | ---: | --- |\n")
    for r in rows: f.write(f"| {r[0]} | {r[1]} | {r[2]:,} | {r[3]}–{r[4]} |\n")
    f.write(f"| **Total** | **{sum(r[1] for r in rows):,}** | | |\n")
print(len(rows), "chunks; max", max(r[1] for r in rows), "words; total", sum(r[1] for r in rows))
