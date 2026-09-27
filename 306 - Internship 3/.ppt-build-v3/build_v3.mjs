import fs from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { FileBlob, PresentationFile } from "@oai/artifact-tool";

const SKILL_DIR = "/Users/Debanjan Mondal/.codex/plugins/cache/openai-primary-runtime/presentations/26.904.11930/skills/presentations";
const RUNTIME_PYTHON = "/Users/Debanjan Mondal/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3";
const workspaceDir = "/Users/Debanjan Mondal/.codex/.chatgpt-projects/g-p-6ab7c6bface08191bafae1e3676762d3";
const sourcePath = "/Users/Debanjan Mondal/Documents/GitHub/Sreetama-Ghosh-Ray/306 - Internship 3/Internship 3 v2.pptx";
const buildDir = path.join(workspaceDir, ".ppt-build-v3");
const finalPath = path.join(workspaceDir, "output-v3", "Internship 3 v3.pptx");
const candidatePath = path.join(buildDir, "candidate-v3.pptx");

await fs.mkdir(buildDir, { recursive: true });
await fs.mkdir(path.dirname(finalPath), { recursive: true });
const presentation = await PresentationFile.importPptx(await FileBlob.load(sourcePath));

// Reduce the deck from 13 to 10 slides. Work backward so indexes stay stable.
for (const index of [10, 4, 1]) {
  presentation.slides.remove(index);
}

// Slide 5: lower the title and remove the extra paragraph break that caused clipping.
const transfersTitle = presentation.resolve("sh/dcbud0ra");
transfersTitle.text.replace("Transfers, Discipline & RABD\n", "Transfers, Discipline & RABD");
transfersTitle.position = { ...transfersTitle.position, top: 118, height: 150 };

// Slide 6: retain the two-column structure but use short, left-aligned copy.
const branchWork = presentation.resolve("sh/n6pwfmd8");
branchWork.text.replace(
  "Visited 27 branches across the region plus RO departments (Retail Loans, Currency Chest) to administer a questionnaire on training effectiveness.",
  "Visited 27 branches and Regional Office departments, including Retail Loans and Currency Chest, to collect responses for the training-effectiveness questionnaire.",
);
branchWork.text.style = { alignment: "left" };

const branchFinding = presentation.resolve("sh/0jydkreh");
branchFinding.text.replace(
  "Staffing varied widely (e.g. Triplicane 2 ran on 2 officers and 1 cashier), directly limiting training time. Employees compared classroom, online and live-streamed training and how far they applied it at work.",
  "Triplicane 2 had two officers and one cashier, which limited available time for training. Employees compared classroom, online and live-streamed learning and their use at work.",
);
branchFinding.text.style = { alignment: "left" };

// Slide 7: qualify staff insights as observations rather than confidential policy review.
const sopCopy = presentation.resolve("sh/2xsjepgb");
sopCopy.text.replace(
  "Staff had to learn common Standard Operating Procedures for documentation, authorisation levels and customer service.",
  "Staff described adapting to common Standard Operating Procedures for documentation, authorisation levels and customer service.",
);
const trainingCopy = presentation.resolve("sh/cnu1kzyd");
trainingCopy.text.replace(
  "Continuous training, not one-time orientation, helped employees adapt with confidence to the merged systems.",
  "Staff described ongoing training as important for adapting to the merged systems.",
);

// Slide 8: fold the former Core Takeaways into Key Learnings.
const learningCopy = presentation.resolve("sh/l036l83y");
const learningSlide = presentation.resolve("sl/m90b6t0r");
learningCopy.delete();
const learnings = [
  "• HR functions cover welfare, leave, transfers, training, internal communication and industrial relations.",
  "• Confidentiality and controlled access protect employee records.",
  "• Staffing and branch workload shape training participation.",
  "• Hybrid learning works best when matched to branch operating conditions.",
  "• The internship strengthened professional communication, research ethics and respectful data collection.",
];
learnings.forEach((text, index) => {
  const row = learningSlide.shapes.add({
    geometry: "textbox",
    position: { left: 295, top: 325 + index * 86, width: 1450, height: 56 },
    fill: "none",
    line: { fill: "none", width: 0 },
  });
  row.text = text;
  row.text.style = {
    typeface: "DM Sans",
    fontSize: 26,
    color: "#07315D",
    alignment: "left",
    autoFit: "shrinkText",
  };
});

// Slide 9: keep all road-map labels readable and aligned above their pins.
const theory = presentation.resolve("sh/cbm5kbyh");
theory.position = { ...theory.position, left: 210, top: 505, width: 310 };
const grounding = presentation.resolve("sh/6t0n6hg7");
grounding.position = { ...grounding.position, left: 475, top: 625, width: 400 };
const growth = presentation.resolve("sh/7u94zmhs");
growth.position = { ...growth.position, left: 1015, top: 620, width: 360 };
const dissertation = presentation.resolve("sh/dcv6dgz2");
dissertation.position = { ...dissertation.position, left: 1505, top: 545, width: 330 };

const { finalizePresentation } = await import(pathToFileURL(
  path.join(SKILL_DIR, "container_tools/artifact_tool_utils.mjs"),
).href);

await (await PresentationFile.exportPptx(presentation)).save(candidatePath);

const stagingDir = path.join(workspaceDir, ".codex-finalizer");
await fs.mkdir(stagingDir, { recursive: true });
const result = await finalizePresentation({
  explicitTotalSlideCount: 10,
  requiredNativeTableOwnerSlides: [],
  workspaceDir,
  candidatePath,
  finalPath,
  pythonExecutable: RUNTIME_PYTHON,
  integrityValidatorPath: path.join(SKILL_DIR, "container_tools/inspect_presentation_package_integrity.py"),
  layoutValidatorPath: path.join(SKILL_DIR, "container_tools/inspect_presentation_layout_geometry.py"),
  layoutArgs: [
    "--expected-slide-size-emu", "18288000,10287000",
    "--validate-bullet-geometry",
    "--validate-heading-fit",
  ],
  verifyArtifactToolImport: true,
  receiptPath: path.join(stagingDir, "Internship 3 v3.recheck.validation.json"),
});

console.log(JSON.stringify(result, null, 2));
