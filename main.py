from pywebminifier import compress_js, compress_css, compress_html

print(compress_js("./file.js", output="out.file.js"))
print(compress_css("./file.css", output="out.file.css"))
print(compress_css("./file.html", output="out.file.html"))