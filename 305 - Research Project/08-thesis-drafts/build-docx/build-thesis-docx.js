// Builds the thesis DOCX (MSSW layout, modelled on recent MSSW project reports) from a Markdown draft.
// Usage (from "305 - Research Project"):
//   NODE_PATH=$(pwd)/08-thesis-drafts/build-docx/node_modules node 08-thesis-drafts/build-docx/build-thesis-docx.js <draft-folder> <source.md> <output.docx> [pages.json]
// pages.json (optional): { "<entry text>": page } used as the starting value of the page-number fields.
const fs = require("fs");
const os = require("os");
const { execFileSync } = require("child_process");
const path = require("path");
const { marked } = require("marked");
const { Resvg } = require("@resvg/resvg-js");
const {
  Document, Paragraph, TextRun, HeadingLevel, AlignmentType, Table, TableRow, TableCell, WidthType,
  ShadingType, ImageRun, PageBreak, VerticalAlign, Bookmark, SimpleField, TabStopType, PageNumber,
  Packer, Footer, UnderlineType, BorderStyle, HeightRule, PageBorderDisplay, PageBorderOffsetFrom, PageBorderZOrder,
} = require("docx");

const SRC_DIR = path.resolve(process.argv[2]);
const MD_PATH = path.join(SRC_DIR, process.argv[3]);
const OUT_PATH = path.join(SRC_DIR, process.argv[4]);
const PAGES = process.argv[5] && fs.existsSync(process.argv[5]) ? JSON.parse(fs.readFileSync(process.argv[5], "utf8")) : {};
const LOGO = path.join(SRC_DIR, "mssw-logo.png");

const STUDENT = "Sreetama Ghosh Ray";
const REGNO = "251578222039";
const GUIDE = "Dr. E. T. EVANGELINE"; // as printed in the department's sample reports
const GUIDE_COVER = "Dr. E. T. EVANGELINE, MBA, M.Phil, Ph.D.";
const MONTH_YEAR = "October 2026";

const FONT = "Times New Roman";
const SZ = 24;
const LINE = { line: 360, lineRule: "auto" };
const LEFT = Number(process.env.LEFT_TW || 1440), RIGHT = Number(process.env.RIGHT_TW || 1440), TOPBOT = Number(process.env.TOPBOT_TW || 1440);
const PARA_AFTER = Number(process.env.PARA_AFTER || 320), TABLE_SZ = Number(process.env.TABLE_SZ || 24), TABLE_LINE = Number(process.env.TABLE_LINE || 360), IMG_W = Number(process.env.IMG_W || 576);
const CELL_TB = Number(process.env.CELL_TB || 240);
const BORDER_SZ = Number(process.env.BORDER_SZ || 12), BORDER_GAP = Number(process.env.BORDER_GAP || 24); // eighths of a point; points from page edge
const USABLE = 11906 - LEFT - RIGHT; // A4

let seq = 0;
const nextId = (p) => `${p}_${++seq}`;
const tocEntries = [], tableEntries = [], figureEntries = [];
let inCh4 = false, afterSource = false;

const bookmarked = (id, children) => { const b = new Bookmark({ id, children }); return [b.start, ...b.children, b.end]; };

function runs(tokens, base, size) {
  const out = [];
  for (const t of tokens || []) {
    if (t.type === "strong") out.push(...runs(t.tokens, { ...base, bold: true }, size));
    else if (t.type === "em") out.push(...runs(t.tokens, { ...base, italics: true }, size));
    else if (t.type === "codespan") out.push(new TextRun({ text: t.text, font: "Courier New", size, ...base }));
    else if (t.type === "text" && t.tokens) out.push(...runs(t.tokens, base, size));
    else if (t.type === "br") out.push(new TextRun({ break: 1, font: FONT, size }));
    else if (t.type === "text") {
      t.text.split("\n").forEach((part, i) => { if (i > 0) out.push(new TextRun({ break: 1, font: FONT, size })); if (part) out.push(new TextRun({ text: part, font: FONT, size, ...base })); });
    }
    else if (t.raw) out.push(new TextRun({ text: t.raw, font: FONT, size, ...base }));
  }
  return out;
}

const hasBreak = (tokens) => (tokens || []).some((t) => t.type === "br" || (t.text && /\n/.test(t.text)) || hasBreak(t.tokens));
let inRefs = false;
const para = (children, o = {}) => new Paragraph({ children, spacing: { ...LINE, after: PARA_AFTER }, alignment: AlignmentType.JUSTIFIED, ...o });

const CAP_TABLE = /^Table\s+([A-Za-z0-9]+\.\d+):\s*(.+)$/;
const CAP_FIG = /^Figure\s+([A-Za-z0-9]+\.\d+):\s*(.+)$/;

function caption(label, title, id) {
  return new Paragraph({
    keepNext: true,
    alignment: AlignmentType.LEFT,
    spacing: { before: 200, after: 120, line: 276, lineRule: "auto" },
    children: bookmarked(id, [new TextRun({ text: `${label} ${title}`, bold: true, font: FONT, size: SZ })]),
  });
}

function renderTable(tok) {
  const n = tok.header.length;
  const longest = tok.header.map((h, i) => Math.max(h.text.length, ...tok.rows.map((r) => r[i].text.split(/\s+/).reduce((m, w) => Math.max(m, w.length), 0) * 1.6 + Math.min(r[i].text.length, 40) * 0.4)));
  const weight = longest.map((l) => Math.max(5, l) ** 0.75);
  const total = weight.reduce((a, b) => a + b, 0);
  const widths = weight.map((x) => Math.max(900, Math.floor((x / total) * USABLE)));
  widths[widths.indexOf(Math.max(...widths))] += USABLE - widths.reduce((a, b) => a + b, 0);
  const align = (i) => (tok.align[i] === "right" ? AlignmentType.RIGHT : tok.align[i] === "center" ? AlignmentType.CENTER : AlignmentType.LEFT);
  const cell = (c, i, head) => new TableCell({
    width: { size: widths[i], type: WidthType.DXA },
    shading: head ? { type: ShadingType.CLEAR, fill: "EDEDED" } : undefined,
    verticalAlign: VerticalAlign.CENTER,
    margins: { top: CELL_TB, bottom: CELL_TB, left: 100, right: 100 },
    children: [new Paragraph({ alignment: align(i), spacing: { line: TABLE_LINE, lineRule: "auto" }, children: runs(c.tokens, head ? { bold: true } : {}, TABLE_SZ) })],
  });
  return new Table({
    width: { size: USABLE, type: WidthType.DXA },
    columnWidths: widths,
    rows: [
      new TableRow({ tableHeader: true, cantSplit: true, children: tok.header.map((c, i) => cell(c, i, true)) }),
      ...tok.rows.map((r) => new TableRow({ cantSplit: true, children: r.map((c, i) => cell(c, i, false)) })),
    ],
  });
}

// Conceptual framework: three predictors -> Training Effectiveness (replaces the text diagram)
function frameworkParagraph() {
  const box = (y, label) => `<rect x="20" y="${y}" width="330" height="72" rx="8" fill="#F2F2F2" stroke="#222" stroke-width="2.5"/><text x="185" y="${y + 46}" font-family="Times New Roman, Liberation Serif, serif" font-size="28" font-weight="bold" text-anchor="middle" fill="#000">${label}</text>`;
  const arrow = (y, ty) => `<line x1="350" y1="${y + 36}" x2="634" y2="${ty}" stroke="#222" stroke-width="2.5" marker-end="url(#a)"/>`;
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="340" viewBox="0 0 1000 340"><defs><marker id="a" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto"><path d="M0,0 L12,6 L0,12 z" fill="#222"/></marker></defs><rect width="1000" height="340" fill="#fff"/>${arrow(20, 135)}${arrow(134, 170)}${arrow(248, 205)}${box(20, "Hybrid Learning")}${box(134, "Trainer Competence")}${box(248, "Learner Engagement")}<rect x="640" y="110" width="340" height="120" rx="8" fill="#F2F2F2" stroke="#222" stroke-width="2.5"/><text x="810" y="160" font-family="Times New Roman, Liberation Serif, serif" font-size="28" font-weight="bold" text-anchor="middle" fill="#000">Training</text><text x="810" y="198" font-family="Times New Roman, Liberation Serif, serif" font-size="28" font-weight="bold" text-anchor="middle" fill="#000">Effectiveness</text></svg>`;
  const r = new Resvg(svg, { fitTo: { mode: "width", value: 2000 } }).render();
  return new Paragraph({ alignment: AlignmentType.CENTER, keepNext: false, spacing: { before: 120, after: 200 }, children: [new ImageRun({ type: "png", data: r.asPng(), transformation: { width: 460, height: 156 }, altText: { name: "framework", description: "Hybrid Learning, Trainer Competence and Learner Engagement as predictors of Training Effectiveness", title: "Conceptual framework" } })] });
}

function renderImage(tok) {
  const svgPath = path.resolve(SRC_DIR, tok.href);
  const rendered = new Resvg(fs.readFileSync(svgPath), { fitTo: { mode: "width", value: 1600 } }).render();
  const wpx = IMG_W, hpx = Math.round((rendered.height / rendered.width) * wpx);
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 60, after: 160 },
    children: [new ImageRun({ type: "png", data: rendered.asPng(), transformation: { width: wpx, height: hpx }, altText: { name: path.basename(svgPath), description: tok.text || "chart", title: tok.text || "chart" } })],
  });
}

function renderBlock(tok) {
  if (tok.type !== "paragraph" && tok.type !== "space") afterSource = false;
  switch (tok.type) {
    case "heading": {
      const text = tok.text;
      if (tok.depth === 1) { inCh4 = /^Chapter 4/.test(text); inRefs = /^References/.test(text); }
      const id = nextId("h");
      if (tok.depth <= 2) tocEntries.push({ text, level: tok.depth, id });
      const level = tok.depth === 1 ? HeadingLevel.HEADING_1 : tok.depth === 2 ? HeadingLevel.HEADING_2 : HeadingLevel.HEADING_3;
      const out = [];
      if (tok.depth === 1) {
        const ch = /^Chapter (\d+) — (.+)$/.exec(text);
        const divider = ch ? [`CHAPTER - ${ch[1]}`, ch[2].toUpperCase()] : /^Appendix A/.test(text) ? ["APPENDIX"] : null;
        out.push(new Paragraph({ children: [new PageBreak()] }));
        if (divider) {
          // separate title page before each chapter and the appendix, as in the department's sample and recent reports;
          // a fixed-height one-cell table keeps the title in the vertical middle of the page
          const none = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
          out.push(new Table({
            width: { size: USABLE, type: WidthType.DXA },
            columnWidths: [USABLE],
            borders: { top: none, bottom: none, left: none, right: none, insideHorizontal: none, insideVertical: none },
            rows: [new TableRow({
              height: { value: 13300, rule: HeightRule.EXACT },
              children: [new TableCell({
                width: { size: USABLE, type: WidthType.DXA },
                verticalAlign: VerticalAlign.CENTER,
                borders: { top: none, bottom: none, left: none, right: none },
                children: divider.map((line) => new Paragraph({
                  alignment: AlignmentType.CENTER,
                  spacing: { before: 120, after: 120, line: 360, lineRule: "auto" },
                  children: [new TextRun({ text: line, font: FONT, size: 52, bold: true })],
                })),
              })],
            })],
          }));
          out.push(new Paragraph({ spacing: { before: 0, after: 0, line: 240, lineRule: "auto" }, children: [new PageBreak()] }));
        }
      }
      out.push(new Paragraph({
        heading: level,
        keepNext: true,
        spacing: { before: tok.depth === 1 ? 0 : 240, after: 160 },
        children: bookmarked(id, [new TextRun({ text: tok.depth === 1 ? text.toUpperCase() : text, font: FONT, bold: true, italics: tok.depth === 3 })]),
      }));
      return out;
    }
    case "paragraph": {
      const plain = (tok.text || "").replace(/\*\*/g, "");
      const strongOnly = /^\*\*[^*].*\*\*$/.test(tok.raw.trim());
      let m;
      if (strongOnly && (m = CAP_TABLE.exec(plain))) {
        afterSource = false;
        const id = nextId("tbl");
        tableEntries.push({ text: `Table ${m[1]}: ${m[2]}`, id });
        return [caption(`Table ${m[1]}:`, m[2], id)];
      }
      if (strongOnly && (m = CAP_FIG.exec(plain))) {
        afterSource = false;
        const id = nextId("fig");
        figureEntries.push({ text: `Figure ${m[1]}: ${m[2]}`, id });
        return [caption(`Figure ${m[1]}:`, m[2], id)];
      }
      if (tok.tokens && tok.tokens.length === 1 && tok.tokens[0].type === "image") { afterSource = false; return [renderImage(tok.tokens[0])]; }
      if (/^\*(?!\*).*\*$/s.test(tok.raw.trim()) && /^Source:/.test(plain.replace(/^\*|\*$/g, ""))) {
        afterSource = true;
        return [new Paragraph({ children: runs(tok.tokens, { italics: true }, 20), alignment: AlignmentType.CENTER, spacing: { after: 160 } })];
      }
      const lead = inCh4 && afterSource ? [new TextRun({ text: "Inference: ", bold: true, font: FONT, size: SZ })] : [];
      afterSource = false;
      if (inRefs) return [para(runs(tok.tokens, {}, SZ), { alignment: AlignmentType.LEFT, indent: { left: 720, hanging: 720 }, spacing: { line: 360, lineRule: "auto", after: 120 } })];
      return [para([...lead, ...runs(tok.tokens, {}, SZ)], { ...(hasBreak(tok.tokens) ? { alignment: AlignmentType.LEFT } : {}), ...(plain.trim().endsWith(":") ? { keepNext: true } : {}) })];
    }
    case "blockquote":
      return tok.tokens.flatMap((t) => t.type === "paragraph"
        ? [new Paragraph({ children: runs(t.tokens, { italics: true }, SZ), indent: { left: 720, right: 720 }, spacing: { ...LINE, after: 160 }, alignment: AlignmentType.JUSTIFIED })]
        : renderBlock(t));
    case "code":
      if (/┐/.test(tok.text)) return [frameworkParagraph()];
      return tok.text.split("\n").map((line, i, a) => new Paragraph({
        alignment: AlignmentType.LEFT,
        indent: { left: 720 },
        keepNext: i < a.length - 1,
        spacing: { line: 276, lineRule: "auto", after: i === a.length - 1 ? 200 : 0 },
        children: [new TextRun({ text: line, font: "Courier New", size: 20 })],
      }));
    case "table":
      return [renderTable(tok), new Paragraph({ text: "", spacing: { after: 120 } })];
    case "list": {
      const out = [];
      let n = tok.ordered ? Number(tok.start || 1) : 0;
      for (const item of tok.items) {
        const first = item.tokens[0];
        const isText = first && (first.type === "text" || first.type === "paragraph");
        const main = isText ? first.tokens || [{ type: "text", text: first.text }] : [];
        const rest = isText ? item.tokens.slice(1) : item.tokens;
        out.push(new Paragraph({
          children: [new TextRun({ text: `${tok.ordered ? n + "." : "•"}\t`, font: FONT, size: SZ }), ...runs(main, {}, SZ)],
          indent: { left: 540, hanging: 360 },
          spacing: { ...LINE, after: 120 },
          alignment: hasBreak(main) ? AlignmentType.LEFT : AlignmentType.JUSTIFIED,
        }));
        for (const ex of rest) {
          if (ex.type === "paragraph") out.push(new Paragraph({ children: runs(ex.tokens, {}, SZ), indent: { left: 540 }, spacing: { ...LINE, after: 120 }, alignment: AlignmentType.JUSTIFIED }));
          else out.push(...renderBlock(ex));
        }
        n++;
      }
      return out;
    }
    default:
      return [];
  }
}

// ---------- front matter (layout follows recent MSSW project reports) ----------
const T = (text, o = {}) => new TextRun({ text, font: FONT, size: SZ, ...o });
const B = (text, o = {}) => T(text, { bold: true, ...o });
const center = (children, o = {}) => new Paragraph({ alignment: AlignmentType.CENTER, children, ...o });
const pb = () => new Paragraph({ children: [new PageBreak()] });
const pageTitle = (t) => center([T(t, { bold: true, underline: { type: UnderlineType.SINGLE } })], { spacing: { after: 360 } });
const sign = (left, right) => new Paragraph({
  spacing: { before: 1200 },
  tabStops: [{ type: TabStopType.RIGHT, position: USABLE }],
  children: [B(left), ...(right ? [B("\t" + right)] : [])],
});

function acknowledgementParas(tokens) {
  const i = tokens.findIndex((t) => t.type === "heading" && t.text === "Acknowledgement");
  if (i < 0) throw new Error("Acknowledgement section not found in the Markdown");
  const out = [];
  const fixName = (ts) => (ts || []).map((t) => { const n = { ...t }; if (typeof t.text === "string") n.text = t.text.replace("Dr. E. T. Evangeline Joshua", "Dr. E. T. Evangeline"); if (t.tokens) n.tokens = fixName(t.tokens); return n; });
  for (let j = i + 1; j < tokens.length && !(tokens[j].type === "heading"); j++) if (tokens[j].type === "paragraph") out.push(para(runs(fixName(tokens[j].tokens), {}, SZ)));
  return out;
}

function reportPage() {
  const dir = path.join(SRC_DIR, "submission");
  const f = fs.existsSync(dir) ? fs.readdirSync(dir).find((x) => /^DB_report.*\.pdf$/.test(x)) : null;
  if (!f) return [];
  const prefix = path.join(os.tmpdir(), "db-report-p1");
  execFileSync("pdftoppm", ["-png", "-r", "200", "-f", "1", "-l", "1", "-singlefile", path.join(dir, f), prefix]);
  const data = fs.readFileSync(prefix + ".png");
  const w = 590, h = Math.round(w * 841.89 / 595.3);
  return [pb(), new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 0, line: 240, lineRule: "auto" }, children: [new ImageRun({ type: "png", data, transformation: { width: w, height: h }, altText: { name: "similarity-report", description: "DrillBit similarity report, first page", title: "Similarity report" } })] })];
}

function front(title, ackTokens) {
  const TITLE = title.toUpperCase();
  const logo = fs.readFileSync(LOGO);
  return [
    center([B(TITLE, { size: 28 })], { spacing: { before: 600, after: 480 } }),
    center([B("PROJECT REPORT")], { spacing: { after: 120 } }),
    center([T("Submitted by")], { spacing: { after: 120 } }),
    center([B(`Ms. ${STUDENT}`)], { spacing: { after: 120 } }),
    center([B(`(Register No: ${REGNO})`)], { spacing: { after: 360 } }),
    center([T("In partial fulfilment of the requirement for the award of the Degree")], { spacing: { after: 120 } }),
    center([B("MASTER OF ARTS IN")], { spacing: { after: 0 } }),
    center([B("HUMAN RESOURCE MANAGEMENT")], { spacing: { after: 240 } }),
    center([T("Under the guidance of")], { spacing: { after: 120 } }),
    center([B(GUIDE_COVER)], { spacing: { after: 60 } }),
    center([B("Head of the Department")], { spacing: { after: 360 } }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 360 }, children: [new ImageRun({ type: "png", data: logo, transformation: { width: 120, height: 118 }, altText: { name: "mssw-logo.png", description: "Madras School of Social Work seal", title: "MSSW seal" } })] }),
    center([B("P.G. DEPARTMENT OF HUMAN RESOURCE MANAGEMENT")], { spacing: { after: 60 } }),
    center([B("MADRAS SCHOOL OF SOCIAL WORK")], { spacing: { after: 60 } }),
    center([T("(AUTONOMOUS)")], { spacing: { after: 60 } }),
    center([T("No. 32, CASA MAJOR ROAD, EGMORE")], { spacing: { after: 60 } }),
    center([T("CHENNAI – 600008")], { spacing: { after: 120 } }),
    center([B(MONTH_YEAR.toUpperCase())]),

    pb(), pageTitle("BONAFIDE CERTIFICATE"),
    para([T("This is to certify that the project titled “"), B(TITLE), T(`” is a bonafide project work done by Ms. ${STUDENT} (Reg No: ${REGNO}), a second year student of M.A. HRM, Madras School of Social Work (Autonomous), Egmore, Chennai in partial fulfilment of the requirement for the Award of the Degree of Master of Arts in Human Resource Management and that the project has not been used previously for the award of any Degree, Diploma, Scholarship, Fellowship or any other project title.`)]),
    sign("Signature of the Guide", "Signature of the HOD"),

    pb(), pageTitle("DECLARATION"),
    para([T(`I, ${STUDENT.toUpperCase()}, final year student of M.A. HRM hereby declare that the thesis entitled “`), B(TITLE), T(`” is the original work done by me under the guidance and supervision of ${GUIDE}, in partial fulfilment of the requirements for the award of the degree of Master of Arts in Human Resource Management, Madras School of Social Work. I further declare that the research work has not been submitted at any other University or Institution, for the award of any degree or diploma or fellowship.`)]),
    sign("Signature of the Guide", "Signature of the Student"),
    new Paragraph({ spacing: { before: 600 }, children: [B("PLACE: CHENNAI")] }),
    new Paragraph({ spacing: { before: 120 }, children: [B(`DATE: ${MONTH_YEAR}`)] }),

    pb(), pageTitle("ACKNOWLEDGEMENT"),
    ...acknowledgementParas(ackTokens),
    ...reportPage(),
  ];
}

const pageOf = (text) => (PAGES[text] !== undefined ? String(PAGES[text]) : "#");
function leader(label, ref, text, indent = 0) {
  return new Paragraph({
    spacing: { after: 100, line: 276, lineRule: "auto" }, indent: { left: indent },
    tabStops: [{ type: TabStopType.RIGHT, position: USABLE, leader: "dot" }],
    children: [T(label), T("\t"), new SimpleField(`PAGEREF ${ref} \\h`, pageOf(text))],
  });
}
const listPage = (title, entries, label) => [pb(), pageTitle(title), ...entries.map((e) => leader(label ? label(e) : e.text, e.id, e.text))];

function contentsPage() {
  const rows = [pb(), pageTitle("TABLE OF CONTENTS"), new Paragraph({
    spacing: { after: 160 },
    tabStops: [{ type: TabStopType.LEFT, position: 1300 }, { type: TabStopType.RIGHT, position: USABLE }],
    children: [B("CHAPTER"), B("\tTITLE"), B("\tPAGE NO")],
  })];
  for (const e of tocEntries) {
    const m = /^Chapter (\d+) — (.+)$/.exec(e.text);
    const first = e.level === 1 ? (m ? m[1] : "") : "";
    const title = e.level === 1 ? (m ? m[2] : e.text).toUpperCase() : e.text;
    rows.push(new Paragraph({
      spacing: { before: e.level === 1 ? 120 : 0, after: 80, line: 276, lineRule: "auto" },
      indent: e.level === 2 ? { left: 1300 + 240 } : { left: 1300, hanging: 1300 },
      tabStops: e.level === 1
        ? [{ type: TabStopType.LEFT, position: 1300 }, { type: TabStopType.RIGHT, position: USABLE }]
        : [{ type: TabStopType.RIGHT, position: USABLE }],
      children: e.level === 1
        ? [T(first, { bold: true }), T("\t" + title, { bold: true }), T("\t"), new SimpleField(`PAGEREF ${e.id} \\h`, pageOf(e.text))]
        : [T(title), T("\t"), new SimpleField(`PAGEREF ${e.id} \\h`, pageOf(e.text))],
    }));
  }
  return rows;
}

async function main() {
  const tokens = marked.lexer(fs.readFileSync(MD_PATH, "utf8"));
  const title = tokens.find((t) => t.type === "heading" && t.depth === 1).text;
  const start = tokens.findIndex((t) => t.type === "heading" && t.depth === 1 && /Chapter 1/.test(t.text));
  const body = tokens.slice(start).flatMap(renderBlock);

  const doc = new Document({
    styles: { default: {
      document: { run: { font: FONT, size: SZ }, paragraph: { spacing: LINE } },
      heading1: { run: { font: FONT, size: 28, bold: true, color: "000000" }, paragraph: { spacing: { before: 0, after: 240 } } },
      heading2: { run: { font: FONT, size: 24, bold: true, color: "000000" }, paragraph: { spacing: { before: 240, after: 160 } } },
      heading3: { run: { font: FONT, size: 24, bold: true, italics: true, color: "000000" }, paragraph: { spacing: { before: 200, after: 120 } } },
    } },
    sections: [{
      properties: { page: {
        margin: { top: TOPBOT, bottom: TOPBOT, left: LEFT, right: RIGHT },
        // frame on every page, as in the MSSW reference reports (about 1/3 inch from the page edge)
        borders: {
          pageBorders: { display: PageBorderDisplay.ALL_PAGES, offsetFrom: PageBorderOffsetFrom.PAGE, zOrder: PageBorderZOrder.FRONT },
          pageBorderTop: { style: BorderStyle.SINGLE, size: BORDER_SZ, color: "000000", space: BORDER_GAP },
          pageBorderBottom: { style: BorderStyle.SINGLE, size: BORDER_SZ, color: "000000", space: BORDER_GAP },
          pageBorderLeft: { style: BorderStyle.SINGLE, size: BORDER_SZ, color: "000000", space: BORDER_GAP },
          pageBorderRight: { style: BorderStyle.SINGLE, size: BORDER_SZ, color: "000000", space: BORDER_GAP },
        },
      } },
      footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 24 })] })] }) },
      children: [
        ...front(title, tokens),
        ...contentsPage(),
        ...listPage("LIST OF TABLES", tableEntries),
        ...listPage("LIST OF CHARTS", figureEntries),
        ...body,
      ],
    }],
  });
  fs.writeFileSync(OUT_PATH, await Packer.toBuffer(doc));
  fs.writeFileSync(OUT_PATH.replace(/\.docx$/, ".entries.json"), JSON.stringify({ toc: tocEntries.map((e) => e.text), tables: tableEntries.map((e) => e.text), figures: figureEntries.map((e) => e.text) }, null, 1));
  console.log("wrote", OUT_PATH, "| contents:", tocEntries.length, "tables:", tableEntries.length, "figures:", figureEntries.length);
}
main().catch((e) => { console.error(e); process.exit(1); });
