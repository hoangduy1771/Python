import os

# can be use to move directory as wel as file

source = "F:\\work\\Workspace\\Python\\Python\\brocodePython\\files\\from\\move.txt"
destination = "F:\\work\\Workspace\\Python\\Python\\brocodePython\\files\\to\\move.txt"

try:
    if os.path.exists(destination):
        print("There was already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")