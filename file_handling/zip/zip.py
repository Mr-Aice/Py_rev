from zipfile import *

file = ZipFile('file_handling/zip/zipping.zip', 'w', ZIP_DEFLATED)

file.write("file_handling/zip/sample.csv")
file.write("file_handling/zip/sample.txt")

file.close()