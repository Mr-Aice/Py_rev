from zipfile import *

file = ZipFile('file_handling/zip/zipping.zip', 'r', ZIP_STORED)


names = file.namelist()


for name in names:
    print(f"Content of this {name}")
    with open(name, 'r') as f:
        print(f"{f.read()}")

file.close()