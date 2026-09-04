import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

OUTPUT_FOLDER = "structure_txt"
LIST_FILENAME = "contents.txt"


def choose_folder(parent):
    return filedialog.askdirectory(parent=parent, title="Select the folder to process")


def create_text_structure(root_path):
    """Mirror the folder tree and create an empty .txt placeholder for each file."""
    output_path = os.path.join(root_path, OUTPUT_FOLDER)
    os.makedirs(output_path, exist_ok=True)

    created_files = 0

    for current_folder, _, files in os.walk(root_path):
        # Do not recurse into the generated output tree.
        if current_folder == output_path or current_folder.startswith(output_path + os.sep):
            continue

        relative_path = os.path.relpath(current_folder, root_path)
        destination = output_path if relative_path == "." else os.path.join(output_path, relative_path)
        os.makedirs(destination, exist_ok=True)

        for filename in files:
            # Preserve the original behavior: skip Windows thumbnail cache files
            # and files whose name contains "SW".
            if filename == "Thumbs.db" or "SW" in filename:
                continue

            placeholder = os.path.join(destination, f"{filename}.txt")
            with open(placeholder, "w", encoding="utf-8"):
                pass
            created_files += 1

    return output_path, created_files


def list_one_level(root_path):
    """Write the immediate folders and files in the selected directory to a text file."""
    items = sorted(os.listdir(root_path), key=str.casefold)
    output_file = os.path.join(root_path, LIST_FILENAME)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("Folders:\n")
        for item in items:
            item_path = os.path.join(root_path, item)
            if os.path.isdir(item_path) and item != OUTPUT_FOLDER:
                file.write(f"[FOLDER] {item}\n")

        file.write("\nFiles:\n")
        for item in items:
            item_path = os.path.join(root_path, item)
            if os.path.isfile(item_path) and item not in {"Thumbs.db", LIST_FILENAME}:
                file.write(f"{item}\n")

    return output_file


def choose_action(parent):
    return simpledialog.askstring(
        "Choose an action",
        "What would you like to do?\n\n"
        "1 - Mirror the folder structure with empty .txt placeholders\n"
        "2 - List the folders and files in the selected directory\n\n"
        "Enter 1 or 2:",
        parent=parent,
    )


def main():
    root = tk.Tk()
    root.withdraw()

    try:
        option = choose_action(root)
        if option is None:
            return
        if option not in {"1", "2"}:
            messagebox.showerror("Invalid option", "Please enter 1 or 2.", parent=root)
            return

        folder = choose_folder(root)
        if not folder:
            return

        if option == "1":
            output_path, count = create_text_structure(folder)
            messagebox.showinfo(
                "Done",
                f"Created {count} placeholder file(s).\n\nOutput folder:\n{output_path}",
                parent=root,
            )
        else:
            output_file = list_one_level(folder)
            messagebox.showinfo(
                "Done",
                f"Folder contents were written to:\n{output_file}",
                parent=root,
            )
    except (OSError, PermissionError) as exc:
        messagebox.showerror("File system error", str(exc), parent=root)
    finally:
        root.destroy()


if __name__ == "__main__":
    main()
