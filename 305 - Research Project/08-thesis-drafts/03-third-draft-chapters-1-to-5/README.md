# Third Thesis Draft — Chapters 1 to 5

**Current source:** [third-draft-source-grammarly-led-humanized.md](third-draft-source-grammarly-led-humanized.md) (Chapters 1–5, one reference list, Appendix A questionnaire, Appendix B questionnaire development). It follows the direct-predictor model reported in the [frozen SPSS output](../../07-research-data-and-analysis/07-v5-spss-output-freeze/README.md).

**Current build:** `hybrid-learning-training-effectiveness-third-draft-final-v4.docx` and `.pdf` (MSSW layout, A4, Times New Roman 12, 1.5 spacing, 1-inch margins, page frame, 83 pages). Rebuild with:

```bash
python3 08-thesis-drafts/build-docx/make_final.py "$(pwd)/08-thesis-drafts/03-third-draft-chapters-1-to-5" third-draft-source-grammarly-led-humanized.md <output-name>
```

## Folder map

| Folder or file | Contents |
| --- | --- |
| `figures/` | Chart SVGs used in Chapter 4 and the SPSS figure-export notes |
| `mssw-logo.png` | Seal used on the cover page |
| `submission/` | The 75-page submission PDF (title page plus pages 9 onward) and the DrillBit similarity report (4%, grade A) |
| `previous-builds/` | Earlier DOCX and PDF builds, kept for comparison |
| `earlier-source-versions/` | Earlier text versions: original draft, prose revision, paraphrased merge, and Grammarly exports |
| `review-and-checks/` | Plagiarism-check chunks and Duplichecker report, paraphrase and humanising chunks, and the review and audit notes |

The first- and second-draft folders are historical snapshots. The document builder lives in [`../build-docx/`](../build-docx/).
