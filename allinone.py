from exiftool import ExifToolHelper
import datetime
import os

def metainfo(path):
    files = os.listdir(path)
    ext = ('.jpeg','.jpg','.png','.JPEG','.JPG','.PNG')
    
    image_list = []
    datearray = []
    
    for filename in files:
        if filename.endswith(ext):
            match = re.search(r'\d{8}[-_]\d{6}', filename)
            if match:
                date = datetime.datetime.strptime(match.group(), "%Y%m%d_%H%M%S" if '_' in match.group() else "%Y%m%d-%H%M%S")
                date = date.strftime("%Y:%m:%d %H:%M:%S")
                image_list.append(filename)
                datearray.append(date)
            else:
                match = re.search(r'\d{8}', filename)
                if match:
                    date = datetime.datetime.strptime(match.group(), "%Y%m%d")
                    date = date.strftime("%Y:%m:%d 12:00:00")
                    image_list.append(filename)
                    datearray.append(date)
    
    return image_list,datearray

def exifupdater(allfiles, datemeta):
    with ExifToolHelper() as et:
        for i, j in zip(allfiles, datemeta):
            et.set_tags(
                i,
                tags={
                    'FileCreateDate': j,
                    'DateTimeOriginal': j,
                    'FileModifyDate': j
                },
                params=["-P", "-overwrite_original"]
            )

        for d in et.get_tags(allfiles, tags=['FileCreateDate', 'FileModifyDate', 'DateTimeOriginal']):
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
