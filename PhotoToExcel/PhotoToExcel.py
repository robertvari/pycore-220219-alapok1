import os
from PIL import Image, ExifTags
from openpyxl import Workbook


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
photo_data = {}

# todo loop through file list
for photo_file in photo_files:
    photo_data[photo_file] = {
        "size": None,
        "date": None,
        "camera": None,
        "iso": None
    }

    img = Image.open(photo_file)
    photo_data[photo_file]["size"] = img.size

    exif_data = img._getexif()

    if not exif_data:
        continue

    # collect exif data from photo
    # add data to photo_data = {}
    photo_data[photo_file]["camera"] = exif_data.get(272)
    photo_data[photo_file]["date"] = exif_data.get(306)
    photo_data[photo_file]["iso"] = exif_data.get(34855)

    pass


# todo create excel sheet
# todo loop through photo_data
    # todo collect data to an excel sheet

# todo save data to photo_data.json

# todo save data to photo_data.xlsx into the photo directory
