from ecommerce.shopping import sales  # import methods(function) from the sales.py module
from pathlib import Path
from time import ctime

"""sales.calculate_items()
sales.calculate_total()

# print(dir(sales))
# print(sales.__name__)
# print(sales.__file__)
# print(sales.__package__)
# print(sales.__spec__)
print('-' * 40)

path = Path("ecommerce/__init__.py")

print(path)
print(path.exists())  # --> to check that path exists or not
print(path.is_file())  # --> to check that path represents file or not
print(path.is_dir())

print(path.name)  # --> it will return the file name
print(path.stem)  # --> it will return the file name without an extension
print(path.suffix)  # --> it will return the file extension .py or .txt etc.
print(path.parent)  # --> it will return the parent folder
print(path.parents)
print(path.parts)

print(path.absolute())  # --> it will write the absolute path of the file
print(path.home())

print('-' * 40)
# but not originally changing the file name and extension
path_2 = path.with_name(
    "file.txt")  # changing the file name and extension using a new path object based on an existing path
path_3 = path.with_suffix(".txt")  # changing the file extension
print(path_2)
print(path_3)"""

dir_path = Path("ecommerce")

print(dir_path.iterdir())

for path in dir_path.iterdir():  # iterate directory
    print(path)

for g_path in dir_path.glob("*.py"):  # glob search
    print("glob search :", g_path)

for rg_path in dir_path.rglob("__init__.py"):  # recursive search
    print("recursive search : ", rg_path)
