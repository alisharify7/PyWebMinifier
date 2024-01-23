import os
import sys


def compress_css(filePath, output):
    """
    This Function Take a css file and compress it,


    :param filePath: full path of css file
    :param output: full path output css file


    """
    if not os.path.exists((output)):
        open(output, "w").close()

    if not os.path.exists(filePath):
        raise FileNotFoundError(f"\n{filePath}\n is not exists")

    with open(filePath, "r") as f:
        # open new file for file
        with open(output, "a", encoding="utf-8") as min_file:
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
                        min_file.write(each[:each.index("/*")])
                        min_file.write(each[each.index("*/") + 2:])
                        continue

                    min_file.write(each[:each.index("/*")])
                    skip = True
                    continue
                min_file.write(each)
