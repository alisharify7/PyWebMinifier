import os
import sys


def compress_css(input_file_path:str, output:str=""):
    """
    """
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"\n{input_file_path}\n is not exists")

    with open(input_file_path, "r") as f:
        # open new file for file
        out_temp_file = ""
        skip = False
        for each in f.readlines():
            if not each.strip():
                continue
            each = each.strip()
            if not "*/" in each and skip:
                continue
            if "*/" in each and skip:
                skip = False
                continue

            if "/*" in each:
                if "*/" in each:
                    out_temp_file += each[:each.index("/*")]
                    out_temp_file += each[each.index("*/") + 2:]
                    continue

                out_temp_file += each[:each.index("/*")]
                skip = True
                continue
            out_temp_file += each

        if output:
            with open(output, mode="w", encoding="utf-8") as f:
                f.write(out_temp_file)
                del out_temp_file
            return True
        else:
            return out_temp_file
