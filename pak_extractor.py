import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
import sys

# ----------------------
# Path to RScanner.exe
# ----------------------
RSCANNER_PATH = r"C:\extractors\New folder (2)\RScanner.exe"

# ----------------------
# Run scanner normally
# ----------------------
def run_scanner(pak_file):
    if not os.path.isfile(RSCANNER_PATH):
        raise FileNotFoundError(f"RScanner.exe not found at:\n{RSCANNER_PATH}")

    # Launch scanner with the .pak file
    subprocess.run([RSCANNER_PATH, pak_file])

# ----------------------
# GUI mode: browse and launch scanner
# ----------------------
def browse_and_run():
    root = tk.Tk()
    root.withdraw()  # hide main window

    pak_file = filedialog.askopenfilename(
        title="Select .pak file to scan",
        filetypes=[("PAK files","*.pak"),("All files","*.*")]
    )
    if not pak_file:
        return

    run_scanner(pak_file)
    messagebox.showinfo("Scanner", f"RScanner launched for:\n{pak_file}")

# ----------------------
# CLI mode
# ----------------------
def cli_mode():
    import argparse
    parser = argparse.ArgumentParser(description="Launcher for RScanner.exe")
    parser.add_argument("--input", required=True, help="Path to .pak file")
    args = parser.parse_args()

    run_scanner(args.input)

# ----------------------
# Main entry
# ----------------------
if __name__ == "__main__":
    if len(sys.argv) > 1:
        # CLI mode
        cli_mode()
    else:
        # GUI mode
        browse_and_run()
