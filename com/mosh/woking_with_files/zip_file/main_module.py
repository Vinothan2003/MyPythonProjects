from pathlib import Path
from zipfile import ZipFile


def main_md():
    print("main module.")


# creating zip file
"""with ZipFile("file.zip", 'w') as file:
    for path in Path("package").rglob("*.*"):
        file.write(path)
print("zip file done")"""

# extracting and reading zip file
with ZipFile("file.zip", 'r') as file:
    print(file.namelist())  # display the file contains in the zip
    file_info = file.getinfo("package/first_sub/first_module.py")
    print(file_info.file_size)
    print(file_info.extract_version)
    print(file_info.compress_size)
    print(file_info.compress_type)
    print(file_info.__class__)
    file.extractall("extracted_files")
