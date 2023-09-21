# os.listdir method to get the list of all files and directories from a specified directory.

import os
# getting the list of all files and directories in the root directory you want to go into
path = "C:\\users\\Prismika"
dir_list = os.listdir(path)

print("Files and directories in "" ,path," ":")
# print the list
print(dir_list)
