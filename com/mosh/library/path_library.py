import datetime
from pathlib import Path
from phone.phone_details import phone_information
from time import ctime
from datetime import datetime
import shutil

# ----------Working with Path---------


# creating path
# Path(r"c:\\user\\kabil\\Pycharm....")
# Path(r"c:\user\kabil\Pycharm....") --> (r)Raw string used to redit of the backslash

# combining
# Path() / Path() combining path
# Path() / "ecommerce" / "__init__" combining path and string

# Path.home() --> return the home dict of current class

phone_information.phone_details()

"""print(dir(phone_information))
print(phone_information.__name__)
print(phone_information.__file__)
print(phone_information.__package__)"""

print(dir())
path = Path("path_library.py")

print(path.home())  # print the home file path
print(path.absolute())  # print the absolute file path
print(path)  # print the file
print(path.exists())  # checking file exists or not
print(path.is_file())  # checking the given path file or not
print(path.is_dir())  # checking the given path directory (folder) or not

print(path.name)  # return the file name and extension
print(path.stem)  # return the file name
print(path.suffix)  # return the file extension

path_2 = path.with_name("path.py")  # rename the file name
print(path_2)

path_3 = path.with_suffix(".txt")  # rename the file extension
print(path_3)

print("-" * 40)
# --------------------------------------------------------------------------------------------------------------------
# -----------Working with directory---------------
path_4 = Path("phone")
# print(path.iterdir()) give the generator object

for p in path_4.iterdir():  # doest not search by pattern and recursively for that we can glob function
    print(p)

for py_g in path_4.glob("*.py"):  # search by pattern
    print('glob:', py_g)

for py_rg in path_4.rglob("*.py"):  # rglob --> search recursively using the specified pattern
    print('rglob :', py_rg)

    # another way is to search recursively

for py_gr in path_4.glob("**/*.py"):
    print("another way recursively : ", py_gr)

path_list = [p for p in path_4.iterdir()]  # iterdir --> does not search by pattern and recursively
path_glob = [pg for pg in path_4.glob("__init__.py")]  # glob --> search by specified pattern
path_recursive = [pr for pr in
                  path_4.rglob("phone_information.py")]  # rglob --> search recursively using the specified pattern

print(path_list)
print(path_glob)
print(path_recursive)
print("-" * 40)
# --------------------------------------------------------------------------------------------------------------------
# -----------Working with file---------------
# it will originally modify the file 

file_path = Path('phone/__init__.py')
print(file_path.exists())
# file_path.rename("phone/__init__.txt") # rename the file (Note: enter the correct path)
# file_path.unlink() # delete the file
print(file_path.stat())  # show the status of the file
print(ctime(file_path.stat().st_ctime))

print(file_path.read_bytes())  # read the file and give the output as byte (prefix b)
print(file_path.read_text())  # read the file and give the output as text
# file_path.write_text("hello my name is vinothan nc") --> used to override the file in text
# file_path.write_bytes() --> used to override the file in byte

# copy the file --> copying the file using path is worst way
# shutil --> used to copying ad moving the huge  file
source_file = Path("phone/__init__.py")
target_file = Path("__init__.py")
# target_file.write_text(source_file.read_text())
shutil.copy(source_file, target_file)

# Get the current time
current_time = datetime.now()

showing_time = current_time.strftime('%Y-%m-%d %I:%M:%S %p')

print(showing_time)
