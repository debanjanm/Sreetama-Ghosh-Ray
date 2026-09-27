import { FileBlob, PresentationFile } from "@oai/artifact-tool";

const sourcePath = "/Users/Debanjan Mondal/Documents/GitHub/Sreetama-Ghosh-Ray/306 - Internship 3/Internship 3 v2.pptx";
const presentation = await PresentationFile.importPptx(await FileBlob.load(sourcePath));
for (const query of ["slide delete remove", "slides collection delete remove", "shape position text alignment", "slide notes delete"]) {
  console.log(`\n--- ${query} ---`);
  console.log(presentation.help("*", { search: query, include: ["index", "notes"], maxChars: 8000 }).ndjson);
}
