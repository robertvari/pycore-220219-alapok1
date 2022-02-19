import os

folder_1_path = r"C:\Work\_PythonSuli\pycore-220219\alapok_1\folder1"
folder_2_path = r"C:\Work\_PythonSuli\pycore-220219\alapok_1\folder2"

# type list
folder_1_content = os.listdir(folder_1_path)
folder_2_content = os.listdir(folder_2_path)

# cast lists to sets
folder_1_set = set(folder_1_content)
folder_2_set = set(folder_2_content)

# get sets intersection and cast back to list
same_files = list(folder_1_set & folder_2_set)

#same_files = list(set(folder_1_content) & set(folder_2_content))
#print(same_files)
