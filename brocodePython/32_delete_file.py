import os
import shutil

try:
    # remove file
    os.remove("F:\\work\\Workspace\\Python\\Python\\brocodePython\\files\\delete\\delete_this.txt")

    # remove empty folder
    os.rmdir("F:\\work\\Workspace\\Python\\Python\\brocodePython\\files\\delete_empty_folder")

    # remove folder that contains files - dangerous - proceed with caution
    shutil.rmtree("F:\\work\\Workspace\\Python\\Python\\brocodePython\\files\\delete_not_empty_folder")

except FileNotFoundError as e:
    print(e)
    print("Can't find the file to delete")
except PermissionError:
    print("You don't have permission to delete that")
