import pathlib


def get_file_info(path: str) -> []:
    """This Function take a full path of a file and return name and extension of that file"""
    p = pathlib.Path(path)
    return 