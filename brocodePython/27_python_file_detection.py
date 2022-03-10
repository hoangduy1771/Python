import os

path = "F:\\work\\Workspace\\Python\\Python\\brocodePython\\files\\text.txt"

if os.path.exists(path):
    print("That path exists")
    if os.path.isfile(path):
        print("That path exists and it is a file")
    elif os.path.isdir(path):
        print("That path exists and it is a directory")
else:
    print("That path does not exist")
