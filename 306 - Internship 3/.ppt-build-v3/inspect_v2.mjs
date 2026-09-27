import { FileBlob, PresentationFile } from "@oai/artifact-tool";

const sourcePath = "/Users/Debanjan Mondal/Documents/GitHub/Sreetama-Ghosh-Ray/306 - Internship 3/Internship 3 v2.pptx";
const presentation = await PresentationFile.importPptx(await FileBlob.load(sourcePath));
const snapshot = await presentation.inspect({
  kind: "slide,textbox,shape,image,table,chart,notes,layout",
  include: "id,slide,name,title,textPreview,text,bbox,bboxUnit,placeholders",
  maxChars: 60000,
});
console.log(snapshot.ndjson);
