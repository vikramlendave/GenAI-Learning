from pypdf import PdfReader

def is_valid_file(path):
    list_valid_extensions = [".PDF"]
    if path.is_file() and path.suffix.upper() in list_valid_extensions:
        return True
    else:
        return False


def read_pdf_and_write_text(read_path, write_path):
    reader = PdfReader(read_path)
    with open(write_path, "a", encoding="utf-8") as f:
        for page in reader.pages:
            f.write(page.extract_text())
        f.close()


def get_all_valid_file_list_from_directory(directory_path, file_list):
    print(directory_path)
    for item in directory_path.glob("*"):
        if item.is_dir():
            get_all_valid_file_list_from_directory(item, file_list)
        else:
            if is_valid_file(item):
                file_list.append(item)
            else:
                print(f"{item} is not a valid file!")
