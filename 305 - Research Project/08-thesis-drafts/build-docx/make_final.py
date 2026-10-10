"""Two-pass build: DOCX -> PDF (LibreOffice) -> read page numbers -> DOCX with those numbers -> PDF.
python3 make_final.py <draft-folder> <source.md> <output-name-without-extension>
Run from '305 - Research Project'. Needs LibreOffice at /Applications/LibreOffice.app and `npm install` run once inside 08-thesis-drafts/build-docx."""
import json, os, re, subprocess, sys, shutil
folder, md, name = os.path.abspath(sys.argv[1]), sys.argv[2], sys.argv[3]
here = os.path.dirname(os.path.abspath(__file__)); root = os.getcwd()
SOFFICE = "/Applications/LibreOffice.app/Contents/MacOS/soffice"
env = dict(os.environ, NODE_PATH=os.path.join(here, "node_modules"))
build = lambda out, pages=None: subprocess.run(["node", os.path.join(here, "build-thesis-docx.js"), folder, md, out] + ([pages] if pages else []), check=True, env=env, capture_output=True)
topdf = lambda docx: subprocess.run([SOFFICE, "--headless", "--convert-to", "pdf", "--outdir", folder, os.path.join(folder, docx)], check=True, capture_output=True)
def page_map(pdf, entries):
    txt = subprocess.run(["pdftotext", "-layout", "-f", "4", "-l", "16", pdf, "-"], capture_output=True, text=True).stdout.split("\f")
    def rows(pg):
        out, buf = [], ""
        for ln in pg.split("\n"):
            s = ln.strip()
            if not s or s in ("TABLE OF CONTENTS", "LIST OF TABLES", "LIST OF CHARTS") or s.startswith("CHAPTER TITLE") or re.fullmatch(r"\d+", s): continue
            buf = (buf + " " + s).strip(); m = re.match(r"^(.*?)\s*(?:\.{3,})?\s*(\d+)$", buf)
            if m: out.append(int(m.group(2))); buf = ""
        return out
    toc, tab, fig = [], [], []
    mode = None
    for pg in txt:
        if "TABLE OF CONTENTS" in pg: mode = toc
        elif "LIST OF TABLES" in pg: mode = tab
        elif "LIST OF CHARTS" in pg: mode = fig
        elif mode is fig and ("CHAPTER - 1" in pg or ("CHAPTER 1" in pg and "INTRODUCTION" in pg)): break
        if mode is not None: mode += rows(pg)
    pm = {}
    for nums, ents in ((toc, entries["toc"]), (tab, entries["tables"]), (fig, entries["figures"])):
        assert len(nums) == len(ents), (len(nums), len(ents))
        pm.update(dict(zip(ents, nums)))
    return pm
build("_pass1.docx"); topdf("_pass1.docx")
entries = json.load(open(os.path.join(folder, "_pass1.entries.json")))
pm = page_map(os.path.join(folder, "_pass1.pdf"), entries)
pj = os.path.join(folder, "_pages.json"); json.dump(pm, open(pj, "w"), ensure_ascii=False)
build(name + ".docx", pj); topdf(name + ".docx")
pm2 = page_map(os.path.join(folder, name + ".pdf"), entries)
print("page numbers stable after pass 2:", pm == pm2, "| pages:", subprocess.run(["pdfinfo", os.path.join(folder, name + ".pdf")], capture_output=True, text=True).stdout.split("Pages:")[1].split()[0])
for f in ("_pass1.docx", "_pass1.pdf", "_pass1.entries.json", "_pages.json", name + ".entries.json"):
    if os.path.exists(os.path.join(folder, f)): os.remove(os.path.join(folder, f))
