from exiftool import ExifToolHelper
from metainfo import metainfo
from exifupdater import exifupdater
import datetime
import os

askPath = input ("Supported Formats\nWindows : C:/path/to/directory\nLinux : /path/to/directory\nEnter Path: ")
try:
    # Change the current working Directory    
    os.chdir(askPath)
    print("Directory changed")
except :
    raise OSError("Invalid Path")
image_list,datearray = metainfo(askPath)
exifupdater(image_list,datearray)
print (len(image_list))
print (len(datearray))
print("Successful")