from pathlib import Path

import utils

"""
Traverse through folder tree and filter pdf files 
Extracts text content from each pdf file, and writes the combined output text file
"""

directory = input("Enter the directory path: ")
output_directory = input("Enter the output directory path: ")

try:
    directory_path = Path(directory)
    if directory_path.exists():
        if directory_path.is_dir():
            file_list=[]
            utils.get_all_valid_file_list_from_directory(directory_path,file_list)
            for file in file_list:
                output_directory_path = Path(output_directory)
                output_directory_path.mkdir(parents=True, exist_ok=True)
                output_text_path = output_directory + "/output_text.txt"
                utils.read_pdf_and_write_text(file,output_text_path)
        else:
            print(f"{directory_path} is not a directory")
    else:
        print("Directory doesn't exist")
except Exception as e:
    print(f"Failed to convert the pdf into text file due to {e}")
