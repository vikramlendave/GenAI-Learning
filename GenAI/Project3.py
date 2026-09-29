from pathlib import Path
import configparser
import utils



def load_config(config_file_path):
    config = configparser.ConfigParser()
    config.read(config_file_path)
    path = Path(config_file_path)
    if not path.is_file():
        raise FileNotFoundError(f"Configuration file not found at: {path}")
    files_read = config.read(path)
    if not files_read:
        raise ValueError(f"Could not parse configuration file: {path}")
    return config

"""
path = input("Enter the path of PDF file: ")
output_path = input("Enter the path of output file: ")
page_no = int(input("Enter the page number: "))
output_path_for_match_text = input("Enter the path of output file for match text: ")
"""
path = "content/Chemistry Questions.pdf"
output_path = "content/output.txt"
page_no = 1
output_path_for_match_text = "content/output_matched_text.txt"

config_path = Path("config.ini")
config = load_config(config_path)
print("Config successfully loaded. Sections:", config.sections())
try:
    path = Path(path)
    if path.exists():
        if utils.is_valid_file(path):
            utils.read_pdf_and_write_text(path, output_path, page_no)
        else:
            print("Invalid file!")
    else:
        print("Path doesn't exist")

    utils.save_matched_text_only(path, output_path_for_match_text, config['SEARCHING']['regrex'])
except Exception as e:
    print(f"Failed to convert the pdf into text file due to {e}")


