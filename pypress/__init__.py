from .compress import compress_js
import pathlib

def main():
    compress_js(filePath=pathlib.Path("./pypress/file.js").absolute(), output=pathlib.Path("./pypress/compress.file.js").absolute())
