from pathlib import Path

import utils

path = input("Enter the path of PDF file: ")
output_path = input("Enter the path of output file: ")
page_no = int(input("Enter the page number: "))
try:
    path = Path(path)
    if path.exists():
        if utils.is_valid_file(path):
            utils.read_pdf_and_write_text(path, output_path, page_no)
        else:
            print("Invalid file!")
    else:
        print("Path doesn't exist")
except Exception as e:
    print(f"Failed to convert the pdf into text file due to {e}")


