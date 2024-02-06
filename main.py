from pywebminifier import compress_js, compress_css

print(compress_js("./file.js", output="out.file.js"))
print(compress_css("./file.css", output="out.file.css"))