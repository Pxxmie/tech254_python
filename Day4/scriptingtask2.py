
import os

# ask the user what they would like the folder to be called
dir_name = input("Please enter the name of the folder: ")

# dir_path = input("Please enter the directory path of where you want the file to be saved?")

# create the directory with the users input
os.mkdir(dir_name)

# full_path = os.path.join(dir_path, dir_name)
#
# os.mkdir(full_path)
#
# print(f"The folder '{dir_name}' has been created in '{dir_path}'.")