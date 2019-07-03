# Pythono3 code to rename multiple files in a directory or folder

import os
from string import digits

# Function to rename multiple files
file_count = 0
folder_path = r"C:\Users\vijay.jhala\Documents\Python Source\prank\\"
for filename in os.listdir(folder_path):
    source_file = folder_path + filename
    remove_digit = str.maketrans('','',digits)
    new_name = filename.translate(remove_digit)
    renamed_file = folder_path + new_name
    os.rename(source_file,renamed_file)
    print("Old Name " + filename)
    print("New Name " + new_name)


