from pathlib import Path

import utils

path = input("Enter the path of the folder (where the PDF files are stored): ")
output_path = input("Enter the path of the folder (where the text files are stored): ")
try:
    path = Path(path)
    if path.exists():
        if utils.is_valid_file(path):
            utils.read_pdf_and_write_text(path, output_path)
        else:
            print("Invalid file!")
    else:
        print("Path doesn't exist")
except Exception as e:
    print(f"Failed to convert the pdf into text file due to {e}")


