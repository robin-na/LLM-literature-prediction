"""
Download PDF and .md files for a list of papers from Google Drive.

PDFs  → extraction_app/pdfs/
.md files → PGG_papers/papers/

Usage:
    python batch_processing/download_papers_for_app.py \
        --pdf-list /path/to/papers_list.txt

papers_list.txt should have one filename per line, e.g.:
    10.1007_bf01074955.pdf
    10.1016_j.jebo.2018.08.008.pdf
"""

import argparse
from pathlib import Path

from googleapiclient.discovery import build

from gdrive_helpers import download_file, find_folder, get_credentials, list_folder_files

REPO_ROOT   = Path(__file__).parent.parent
MD_OUT_DIR  = REPO_ROOT / "PGG_papers" / "papers"
PDF_OUT_DIR = REPO_ROOT / "extraction_app" / "pdfs"

MD_FOLDER_NAME   = "papers_markdown"
PDF_FOLDER_NAMES = ["papers_pdf", "PGG papers", "papers", "PDF"]


def search_file_globally(service, filename):
    """Search for a file by exact name across all drives."""
    results = service.files().list(
        q=f"name = '{filename}' and trashed = false",
        fields="files(id, name)",
        pageSize=10,
        includeItemsFromAllDrives=True,
        supportsAllDrives=True,
    ).execute()
    return results.get("files", [])


def main():
    parser = argparse.ArgumentParser(
        description="Download PDFs and .md files for a paper list from Google Drive."
    )
    parser.add_argument(
        "--pdf-list",
        type=Path,
        required=True,
        help="Text file with one PDF filename per line (e.g. 10.1007_bf01074955.pdf)",
    )
    args = parser.parse_args()

    pdf_names = [line.strip() for line in args.pdf_list.read_text().splitlines() if line.strip()]
    print(f"Loaded {len(pdf_names)} paper filenames from {args.pdf_list}")

    MD_OUT_DIR.mkdir(parents=True, exist_ok=True)
    PDF_OUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Authenticating with Google Drive...")
    creds = get_credentials()
    service = build("drive", "v3", credentials=creds)

    # ── Index .md folder ─────────────────────────────────────────────────────
    print(f"\nSearching for '{MD_FOLDER_NAME}' folder...")
    md_folders = find_folder(service, MD_FOLDER_NAME)
    md_drive_files = {}
    if md_folders:
        md_folder_id = md_folders[0]["id"]
        print(f"  Found: {md_folders[0]['name']} (id={md_folder_id})")
        md_drive_files = list_folder_files(service, md_folder_id)
        print(f"  {len(md_drive_files)} files in folder.")
    else:
        print(f"  WARNING: '{MD_FOLDER_NAME}' folder not found. Will skip .md downloads.")

    # ── Index PDF folder (first name that resolves) ───────────────────────────
    pdf_drive_files = {}
    for folder_name in PDF_FOLDER_NAMES:
        print(f"\nSearching for '{folder_name}' PDF folder...")
        folders = find_folder(service, folder_name)
        if folders:
            fid = folders[0]["id"]
            print(f"  Found: {folders[0]['name']} (id={fid})")
            contents = list_folder_files(service, fid)
            pdf_drive_files = {k: v for k, v in contents.items() if k.lower().endswith(".pdf")}
            print(f"  {len(pdf_drive_files)} PDF files indexed.")
            break
    else:
        print("  No dedicated PDF folder found — will fall back to global search per file.")

    # ── Download ──────────────────────────────────────────────────────────────
    md_downloaded, md_skipped, md_missing = [], [], []
    pdf_downloaded, pdf_skipped, pdf_missing = [], [], []

    for pdf_name in sorted(pdf_names):
        stem = Path(pdf_name).stem
        md_name = stem + ".md"

        # .md file
        md_dest = MD_OUT_DIR / md_name
        if md_dest.exists():
            md_skipped.append(md_name)
        elif md_name in md_drive_files:
            print(f"  [md]  Downloading {md_name}...")
            download_file(service, md_drive_files[md_name], md_dest)
            md_downloaded.append(md_name)
        else:
            md_missing.append(md_name)

        # PDF file
        pdf_dest = PDF_OUT_DIR / pdf_name
        if pdf_dest.exists():
            pdf_skipped.append(pdf_name)
        elif pdf_name in pdf_drive_files:
            print(f"  [pdf] Downloading {pdf_name}...")
            download_file(service, pdf_drive_files[pdf_name], pdf_dest)
            pdf_downloaded.append(pdf_name)
        else:
            print(f"  [pdf] Searching globally for {pdf_name}...")
            hits = search_file_globally(service, pdf_name)
            if hits:
                print(f"         Found via global search. Downloading...")
                download_file(service, hits[0]["id"], pdf_dest)
                pdf_downloaded.append(pdf_name)
            else:
                pdf_missing.append(pdf_name)

    # ── Summary ───────────────────────────────────────────────────────────────
    print(f"\n{'='*60}")
    print(f"Markdown (.md) — output: {MD_OUT_DIR}")
    print(f"  Downloaded : {len(md_downloaded)}")
    print(f"  Skipped    : {len(md_skipped)} (already existed)")
    print(f"  Not found  : {len(md_missing)}")

    print(f"\nPDF — output: {PDF_OUT_DIR}")
    print(f"  Downloaded : {len(pdf_downloaded)}")
    print(f"  Skipped    : {len(pdf_skipped)} (already existed)")
    print(f"  Not found  : {len(pdf_missing)}")

    if md_missing:
        print("\n.md files not found:")
        for f in md_missing:
            print(f"  {f}")
    if pdf_missing:
        print("\nPDF files not found:")
        for f in pdf_missing:
            print(f"  {f}")


if __name__ == "__main__":
    main()
