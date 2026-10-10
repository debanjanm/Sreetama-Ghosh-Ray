"""Split third-draft-source.md into plain-text chunks for Duplichecker (limit 10,000 characters per check).

Run from this folder:  python3 make_chunks.py
Outputs chunk-NN-<chapter>.txt, chunk-index.md and (if missing) score-log.md.
"""
import re, glob, os

CAP = 9400  # characters per chunk; Duplichecker limit is 10,000
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "..", "earlier-source-versions", "third-draft-source.md")
SKIP_H1 = ("References", "Appendix A")  # bibliography and the questionnaire itself always match

def clean(t):
    t = re.sub(r"`([^`]*)`", r"\1", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"\1", t)
    t = re.sub(r"\*([^*\s][^*]*)\*", r"\1", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)
    return re.sub(r"[ \t]+", " ", t).strip()

def blocks():
    """Yield (chapter_label, section_heading, paragraph_text, source_line)."""
    chap, sec, in_code = None, "", False
    for n, line in enumerate(open(SRC, encoding="utf8"), 1):
        s = line.rstrip("\n")
        if s.startswith("```"):
            in_code = not in_code; continue
        if in_code or not s.strip(): continue
        if s.startswith("# "):
            h = s[2:].strip()
            chap = None if h.startswith(SKIP_H1) or not re.match(r"(Chapter|Appendix B)", h) else re.sub(r"[^A-Za-z0-9]+", "-", h.split("—")[0]).strip("-").lower()
            sec = h; continue
        if s.startswith("#"):
            sec = s.lstrip("# ").strip(); continue
        if chap is None: continue
        if s.startswith(("|", "!", ">", "    ")) or re.match(r"\*\*(Table|Figure) ", s) or s.startswith("*Source") or s.strip() == "---":
            continue
        yield chap, sec, clean(re.sub(r"^\s*(\d+\.|[-•])\s+", lambda m: m.group(1) + " ", s)), n

def split_long(p):
    out, cur = [], ""
    for sent in re.split(r"(?<=[.?!])\s+", p):
        if len(cur) + len(sent) + 1 > CAP and cur: out.append(cur); cur = sent
        else: cur = (cur + " " + sent).strip()
    return out + [cur]

for f in glob.glob(os.path.join(HERE, "chunk-*.txt")): os.remove(f)
chunks, cur = [], None
for chap, sec, text, ln in blocks():
    for piece in split_long(text):
        if cur is None or cur["chap"] != chap or len(cur["text"]) + len(piece) + 2 > CAP:
            cur = {"chap": chap, "text": "", "sec0": sec, "sec1": sec, "l0": ln, "l1": ln}; chunks.append(cur)
        cur["text"] += ("\n\n" if cur["text"] else "") + piece
        cur["sec1"], cur["l1"] = sec, ln

rows = []
for i, c in enumerate(chunks, 1):
    name = f"chunk-{i:02d}-{c['chap']}.txt"
    open(os.path.join(HERE, name), "w", encoding="utf8").write(c["text"] + "\n")
    rows.append((i, name, len(c["text"]), len(c["text"].split()), c["sec0"], c["sec1"], c["l0"], c["l1"]))

tot_c, tot_w = sum(r[2] for r in rows), sum(r[3] for r in rows)
with open(os.path.join(HERE, "chunk-index.md"), "w", encoding="utf8") as f:
    f.write("# Chunk index\n\nGenerated from `third-draft-source.md` by `make_chunks.py`. Lines refer to that file.\n\n")
    f.write("| # | File | Characters | Words | From section | To section | Source lines |\n| --- | --- | ---: | ---: | --- | --- | --- |\n")
    for r in rows: f.write(f"| {r[0]} | {r[1]} | {r[2]:,} | {r[3]:,} | {r[4]} | {r[5]} | {r[6]}–{r[7]} |\n")
    f.write(f"| | **Total** | **{tot_c:,}** | **{tot_w:,}** | | | |\n")
log = os.path.join(HERE, "score-log.md")
if not os.path.exists(log):
    with open(log, "w", encoding="utf8") as f:
        f.write("# Duplichecker score log\n\nFinal score = characters-weighted average of the chunk scores. Target: below 10%.\n\n")
        f.write("| # | Chars | Run 1 % | Top matched sources / sentences | Action taken | Run 2 % |\n| ---: | ---: | ---: | --- | --- | ---: |\n")
        for r in rows: f.write(f"| {r[0]} | {r[2]:,} | | | | |\n")
        f.write("| | **Weighted** | | | | |\n")
print(len(rows), "chunks;", f"{tot_c:,} chars;", f"{tot_w:,} words;", "max chunk", max(r[2] for r in rows))
