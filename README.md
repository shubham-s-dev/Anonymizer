# The File Anonymizer (Confidentiality Cloak)

A Python automation tool designed for **Data Privacy**. It automatically scans a folder of sensitive documents, renames them with random unique IDs to hide identities, and generates a secure **Excel Key-Map** to track original vs. hidden names.

## Use Case
Perfect for HR departments or Legal teams who need to share documents (Resumes, Case Files) with external consultants without revealing personal identities (GDPR/Privacy Compliance).

## How It Works

1.  **Scan:** Detects `.pdf`, `.docx`, and `.xlsx` files in the target folder.
2.  **Generate ID:** Creates a unique 4-digit random code for each file (e.g., `Candidate_4921.docx`).
3.  **Rename:** Uses OS commands to rename files instantly.
4.  **Map:** Saves the link between the *Original Name* and *Hidden Name* in a local `Secret_Map.xlsx` file.

## Logic Highlights

* **Self-Preservation:** The script intelligently skips its own report file (`Secret_Map.xlsx`) to avoid errors.
* **Type Safety:** Handles distinct file extensions dynamically.
* **Audit Trail:** Provides a full report of all changes.

## How to Run

1.  Put your files in the `sensitive_data` folder.
2.  Run the script:
    ```bash
    python anonymizer.py
    ```
3.  Check the folder: Files are renamed, and a new Excel map is created.

---
*Built with Python `os`, `random`, and `pandas`.*