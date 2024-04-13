from com.mosh.work_package.package.first_sub import first_module
from pathlib import Path
from time import ctime
import shutil

def main_md():
    print("main module.")


if __name__ == '__main__':
    main_md()
    first_module.first_md()

    path = Path("package/__init__.py")
    # -__________working with Path____________-
    print(path.exists())
    print(path.is_file())
    print(path.is_dir())

    print(path.name)
    print(path.stem)
    print(path.suffix)
    print(path.parent)
    print(path.parents)
    print(path.parts)

    print(path.with_name("init.txt"))
    print(path.with_suffix('.jpg'))
    print(path.with_stem('constructor'))
    # print(path.with_segments())
    # -__________working with dir____________-
    directory = Path("package")
    print(directory.exists())
    # print(directory.mkdir())
    # print(directory.rmdir())
    # print(directory.rename())

    # print(directory.iterdir())
    direct_iter = [p for p in directory.iterdir()]
    print(direct_iter)
    direct_glob = [p for p in directory.glob("*.py")]
    print(direct_glob)
    direct_rglob = [p for p in directory.rglob("*.py")]
    print(direct_rglob)
    for p in directory.iterdir():
        print(p)

    # -__________working with file____________-
    file = Path("package/__init__.py")
    print(file.exists())
    # file.rename("package/__init__.py")
    # file.unlink()

    print(file.stat())
    print(ctime(file.stat().st_ctime))

    source = Path("package/first_sub/__init__.py")
    target = Path("package/__init__.py")

    # target.write_text(source.read_text())

    shutil.copy(source, target)
