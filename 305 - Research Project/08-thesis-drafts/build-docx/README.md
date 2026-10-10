# Thesis document builder

Builds the MSSW-format Word file and PDF from a Markdown draft.

- `build-thesis-docx.js` — Markdown to DOCX (cover, certificate, declaration, acknowledgement, contents and lists, chapters, page frame).
- `make_final.py` — two-pass build: DOCX, PDF through LibreOffice, read the page numbers, rebuild with them, check they are stable.
- `package.json` and `package-lock.json` — the three Node packages used (`docx`, `marked`, `@resvg/resvg-js`).

Set-up (once): `cd 08-thesis-drafts/build-docx && npm install`. LibreOffice must be installed at `/Applications/LibreOffice.app`. `node_modules/` is not committed.
