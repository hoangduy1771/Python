# basic functions to copy a file in shutil module:
#   copyfile() = copies contents of a file
#   copy() = copyfile() + permission mode + destination can be a directory
#   copy2() = copy() + copies metadata (file's creation and modification times)

import shutil
source = 'F:\\work\\Workspace\\Python\\Python\\brocodePython\\files\\file_to_copy.txt'
destination = 'F:\\work\\Workspace\\Python\\Python\\brocodePython\\files\\clone_of_copy.txt'
shutil.copy(source, destination) # source and destination
