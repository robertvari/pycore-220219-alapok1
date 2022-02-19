import os

# r = raw string
my_folder_path = r"C:\Work\_PythonSuli\pycore-220219\alapok_1"

folder_content = os.listdir(my_folder_path)
print(folder_content)
print(len(folder_content))
print(folder_content[-1])