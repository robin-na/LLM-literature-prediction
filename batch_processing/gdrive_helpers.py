"""Shared Google Drive auth and file-access helpers."""

import io
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

_SCRIPT_DIR      = Path(__file__).parent
CREDENTIALS_FILE = _SCRIPT_DIR / "gdrive_credentials.json"
TOKEN_FILE       = _SCRIPT_DIR / "gdrive_token.json"


def get_credentials():
    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not CREDENTIALS_FILE.exists():
                raise FileNotFoundError(
                    f"Credentials file not found: {CREDENTIALS_FILE}\n"
                    "See download_papers_md.py docstring for one-time setup instructions."
                )
            flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_FILE), SCOPES)
            creds = flow.run_local_server(port=0)
        TOKEN_FILE.write_text(creds.to_json())
    return creds


def find_folder(service, name):
    """Return a list of Drive folder dicts matching *name* (shared-with-me first)."""
    for shared in (True, False):
        q = f"name = '{name}' and mimeType = 'application/vnd.google-apps.folder'"
        if shared:
            q += " and sharedWithMe = true"
        results = service.files().list(
            q=q,
            fields="files(id, name)",
            pageSize=10,
            includeItemsFromAllDrives=True,
            supportsAllDrives=True,
        ).execute()
        files = results.get("files", [])
        if files:
            return files
    return []


def list_folder_files(service, folder_id):
    """Return {filename: file_id} for all direct children of folder_id."""
    files = {}
    page_token = None
    while True:
        params = dict(
            q=f"'{folder_id}' in parents and trashed = false",
            fields="nextPageToken, files(id, name)",
            pageSize=1000,
            includeItemsFromAllDrives=True,
            supportsAllDrives=True,
        )
        if page_token:
            params["pageToken"] = page_token
        response = service.files().list(**params).execute()
        for f in response.get("files", []):
            files[f["name"]] = f["id"]
        page_token = response.get("nextPageToken")
        if not page_token:
            break
    return files


def download_file(service, file_id, dest_path):
    request = service.files().get_media(fileId=file_id)
    with open(dest_path, "wb") as fh:
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            _, done = downloader.next_chunk()
