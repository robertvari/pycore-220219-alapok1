import os

photo_folder = input("Where are your photos?")

# check if path exists
                # False                       print this!
assert os.path.exists(photo_folder), "This folder does not exist!"

# check if path == folder
assert os.path.isdir(photo_folder), "Path must be a folder."


# todo list folder for content os.listdir()

# todo filter result. Only accept .jpg files photo_files = []

# todo loop through file list
    # todo collect exif data from photo
