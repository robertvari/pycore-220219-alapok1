import os

# photo_folder = input("Where are your photos?")
photo_folder = "C:/Work/_PythonSuli/pycore-220219/photos"

# check if path exists
                # False                       print this!
assert os.path.exists(photo_folder), "This folder does not exist!"

# check if path == folder
assert os.path.isdir(photo_folder), "Path must be a folder."


# list folder for content os.listdir()
folder_content = os.listdir(photo_folder)


# filter result. Only accept .jpg and .png files photo_files = []
photo_files = []
allowed_extensions = [".jpg", ".jpeg", ".png"]

for i in folder_content:
    file_full_path = os.path.join(photo_folder, i)
    if os.path.isdir(file_full_path):
        continue

    name, ext = os.path.splitext(file_full_path)

    if ext.lower() in allowed_extensions:
        photo_files.append(file_full_path)


# todo create a dictionary for store photo data: photo_data = {}

# todo loop through file list
    # todo collect exif data from photo
    # todo add data to photo_data = {}


# todo create excel sheet
# todo loop through photo_data
    # todo collect data to an excel sheet

# todo save data to photo_data.json

# todo save data to photo_data.xlsx into the photo directory
