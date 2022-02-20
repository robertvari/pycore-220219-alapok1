import os

photo_folder = input("Where are your photos?")

# check if path exists
                # False                       print this!
assert os.path.exists(photo_folder), "This folder does not exist!"

# check if path == folder
assert os.path.isdir(photo_folder), "Path must be a folder."


# todo list folder for content os.listdir()

# todo filter result. Only accept .jpg files photo_files = []

# todo create a dictionary for store photo data: photo_data = {}

# todo loop through file list
    # todo collect exif data from photo
    # todo add data to photo_data = {}


# todo create excel sheet
# todo loop through photo_data
    # todo collect data to an excel sheet

# todo save data to photo_data.json

# todo save data to photo_data.xlsx into the photo directory
