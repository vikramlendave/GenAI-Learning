from pathlib import Path

from pypdf import PdfReader

import utils

path = input("Enter the path of the folder (where the PDF files are stored): ")

try:
    path = Path(path)
    if path.exists():
        if utils.is_valid_file(path):
            reader = PdfReader(path)
            with open("content/output.txt", "w", encoding="utf-8") as f:
                for page in reader.pages:
                    f.write(page.extract_text())
                f.close()
        else:
            print("Invalid file!")
    else:
        print("Path doesn't exist")
except Exception as e:
    print(f"Failed to convert the pdf into text file due to {e}")


