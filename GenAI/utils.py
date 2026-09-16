def is_valid_file(path):
    list_valid_extensions = [".PDF"]
    if path.is_file() and path.suffix.upper() in list_valid_extensions:
        return True
    else:
        return False