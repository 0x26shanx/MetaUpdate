from exiftool import ExifToolHelper
import datetime
import os

def metainfo(path):
    str = os.listdir(path)
    ext = ('.jpeg','.jpg','.png','.JPEG','.JPG','.PNG')
    
    image_list = []
    datearray = []
    
    for j in str:
        digit=0
        for ch in j:
            if ch.isdigit():
                digit=digit+1
        if digit >= 14:
            if j.endswith(ext):
                image_list.append(j)

    for i in image_list:
        for tp in ext:
            i = i.replace(tp,'')
        i = i.split("_")
        for splitted in i:
            if splitted.startswith("20") == True:
                if len(splitted) == 15:
                    splitted = splitted[:15]
                    date = datetime.datetime.strptime(splitted, "%Y%m%d-%H%M%S")
                    date = date.strftime("%Y:%m:%d %H:%M:%S")
                    datearray.append(date)
                elif len(splitted) == 19:
                    splitted = splitted[:19]
                    date = datetime.datetime.strptime(splitted, "%Y-%m-%d-%H-%M-%S")
                    date = date.strftime("%Y:%m:%d %H:%M:%S")
                    datearray.append(date)
    return image_list,datearray

def exifupdater(allfiles,datemeta):

    for i,j in zip(allfiles,datemeta):
        with ExifToolHelper() as et:
            et.set_tags(
            i,
            tags={
                'FileCreateDate':  j,
                'DateTimeOriginal':  j,
                'FileModifyDate':  j},
            params=["-P", "-overwrite_original"]
        )

    with ExifToolHelper() as et:
        for d in et.get_tags(allfiles,tags=['FileCreateDate','FileModifyDate','DateTimeOriginal']):
            for k, v in d.items():
                print(f"{k} = {v}")

askPath = input ("Supported Formats\nWindows : C:/path/to/directory\nLinux : /path/to/directory\nEnter Path: ")
try:
    # Change the current working Directory    
    os.chdir(askPath)
    print("Directory changed")
except :
    raise OSError("Invalid Path")
image_list,datearray = metainfo(askPath)
exifupdater(image_list,datearray)
#print (len(image_list))
#print (len(datearray))
print("Successful")
