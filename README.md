# Folders & Files Logger

A small Windows utility for quickly documenting the contents and structure of folders.

It provides two modes:

1. **Mirror a folder tree with empty `.txt` placeholders** — recreates the selected directory structure inside `structure_txt` and creates an empty `.txt` file for each source file.
2. **List one directory level** — creates `contents.txt` containing the immediate folders and files in the selected directory.

## Features

- Simple graphical folder picker
- No hard-coded user or drive paths
- Preserves nested folder structure in mirror mode
- Ignores `Thumbs.db`
- Preserves the original filter that skips filenames containing `SW` in mirror mode
- Sorts one-level listings alphabetically
- Shows a confirmation dialog when the operation finishes

## Requirements

- Windows
- Python 3.9 or newer
- Tkinter (included with standard Python installations for Windows)

No third-party Python packages are required.

## Usage

### Quick start

Double-click:

```text
run_folders_files_logger.bat
```

Then choose option `1` or `2` and select the folder you want to process.

### Run directly with Python

```bash
python folders_files_logger.py
```

## Output

### Option 1 — Folder structure mirror

The app creates a `structure_txt` folder inside the selected directory. The hierarchy is mirrored and each original file is represented by an empty `.txt` placeholder.

For example:

```text
Selected folder/
├── Documents/
│   └── report.pdf
└── image.png
```

becomes:

```text
Selected folder/
└── structure_txt/
    ├── Documents/
    │   └── report.pdf.txt
    └── image.png.txt
```

### Option 2 — One-level listing

The app creates `contents.txt` in the selected directory with separate sections for folders and files.

## Notes

The mirror mode intentionally skips files named `Thumbs.db` and filenames containing `SW`, matching the behavior of the original personal utility.

## Project background

This utility was created to speed up repetitive file-management and folder-documentation tasks on Windows.
