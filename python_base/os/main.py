"""
    Creates a pretty fs structure in projects fs_tree folder.
"""

import os


PATH = os.path.join(os.path.dirname(
    os.path.abspath("../fs_tree")), "../fs_tree")
print(type(__file__))


def create_folders(path, names):
    if os.access(path, os.F_OK):
        for name in names:
            os.mkdir(os.path.join(path, name))


def create_files(path, names):
    for name in names:
        try:
            os.mknod(os.path.join(path, name), mode=0o600)
        except OSError as err:
            print("No write permissions")


def create_pretty_tree(path, high_folders_count):
    dir_names = []
    file_names = []
    for i in range(high_folders_count):
        dir_names.append(chr(97 + i))
        file_names.append(str(i))
    create_folders(path, dir_names)
    create_files(path, file_names)
    for _dir in dir_names:
        abs_dir_path = os.path.join(path, _dir)
        create_pretty_tree(abs_dir_path, ord(_dir)-97)


def view_fs_tree(path, indent="   "):
    viewer = "|--- "
    for item in os.scandir(path):
        if item.is_file():
            print(indent + "{}{} (file)".format(viewer, item.name))
        if item.is_dir():
            print(indent + "{}{} (dir)".format(viewer, item.name))
            view_fs_tree(item.path, indent=indent + "   ")


def clear_tree(path):
    for root, dirs, files, rootfd in os.fwalk(path, topdown=False):
        for name in files:
            os.unlink(name, dir_fd=rootfd)
        for name in dirs:
            os.rmdir(name, dir_fd=rootfd)


if __name__ == '__main__':
    clear_tree(PATH)
    create_pretty_tree(PATH, 5)
    view_fs_tree(PATH)
    clear_tree(PATH)
