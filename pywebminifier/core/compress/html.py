import os
from . import css, js


def compress_html(input_file_path:str, output:str=""):
    """
    """
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"\n{input_file_path}\n is not exists")

    with open(input_file_path, "r") as f:
        # open new file for file
        out_temp_file = ""
        skip = False

        internal_css = False
        internal_css_temp = None
        internal_js = False
        internal_js_temp = None


        for each in f.readlines():
            if not each.strip():
                continue
            each = each.strip()
            if "<style>" in each and "</style>" in each:
                inside_css = each[each.index("<style>")+7:each.index("</style>")]
                each += f"<style>{css.compress_css(inside_css)}</style>"
                continue
            if "<style>" in each:
                internal_css = True
                internal_css_temp += each[each.index("<style>"+7):]
                continue

            if "</style>" in each:
                internal_css_temp += each[:each.index("</style>")]
                each += f"<style>{css.compress_css(internal_css_temp)}</style>"
                internal_css_temp = None
                internal_css = False

            if internal_css:
                internal_css_temp += each
                continue

            if "<script>" in each and "</script>" in each:
                inside_js = each[each.index("<script>")+8:each.index("</script>")]
                each += f"<script>{js.compress_js(inside_js)}</script>"
                continue

            if "<script>" in each:
                internal_js = True
                internal_js_temp += each[each.index("<script>"+8):]
                continue

            if "</script>" in each:
                internal_js_temp += each[:each.index("</script>")]
                each += f"<script>{js.compress_js(internal_js_temp)}</script>"
                internal_js_temp = None
                internal_js = False

            if internal_js:
                internal_js_temp += each
                continue


            if not "-->" in each and skip:
                continue
            if "-->" in each and skip:
                skip = False
                continue

            if "<!--" in each:
                if "-->" in each:
                    out_temp_file += each[:each.index("<!--")]
                    out_temp_file += each[each.index("-->") + 3:]
                    continue

                out_temp_file += each[:each.index("<!--")]
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
