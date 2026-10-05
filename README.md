[automation-scripts README.md](https://github.com/user-attachments/files/33070872/automation-scripts.README.md)
# automation-scripts# automation-scripts

Standalone Python scripts that automate repetitive work: Outlook attachments, Excel processing, PDF extraction, file organization. Each script runs on its own — no framework to install, just run the one you need.

> **Note:** rename the files below first (GitHub web UI: click file → pencil icon → rename). The old names had spaces, typos, and one shadowed a real library.

| Old name | New name | What it does |
| -------- | -------- | ------------ |
| `outlook_attachment_download.py` | — | Downloads Outlook attachments, including from subfolders |
| `download_attachments_from_subfolder.py` | — | (merge into the above if it duplicates it) |
| `outlook_msg.py` | — | Reads/parses Outlook .msg files |
| `Excel Chunk.py` | `excel_chunk.py` | Splits large Excel files into smaller chunks |
| `CopyandMove.py` | `copy_and_move.py` | Batch copy/move/organize files |
| `cleaning.py` | — | Data cleaning helpers |
| `pdfplumber.py` | `pdf_extractor.py` | Extracts text/tables from PDFs (old name shadowed the pdfplumber library) |
| `searachcondafiles.py` | `search_conda_files.py` | Searches files across conda environments (typo fixed) |
| `import shutil.py` | `file_helpers.py` | Small file utilities (rename to match actual contents) |
| `demo.py` | — | Usage demo |

## Run

```bash
python <script_name>.py
```

Most scripts take input/output paths as arguments — check the header comments at the top of each file.

## Requirements

- Python 3.10+
- Install per script as needed: `pandas`, `openpyxl`, `pdfplumber`, `pywin32` (for Outlook automation on Windows)

```bash
pip install pandas openpyxl pdfplumber
```

## License

MIT © Jeff Rotar
