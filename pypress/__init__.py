from .compress import compress_css
import pathlib

def main():
    compress_css(filePath=pathlib.Path("./pypress/file.css").absolute(), output=pathlib.Path("./pypress/compress.file.css").absolute())
