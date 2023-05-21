import datetime
import os
import re

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

    # for i in str:
    #     if i.endswith(ext):
    #         i = i.split("-")            
    #         for splitted in i:
    #             if splitted.startswith("20") == True:
    #                 splitted = splitted[:8]
    #                 date = datetime.datetime.strptime(splitted, "%Y%m%d")
    #                 date = date.strftime("%Y:%m:%d 12:00:00")
    #                 datearray.append(date)
    # return str,datearray

    # for i in image_list:
    #     if i.endswith(ext):
    #         str = i
    #         digit=0
    #         for ch in str:
    #             if ch.isdigit():
    #                 digit=digit+1
