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
                if len(splitted) == 8:
                    splitted = splitted[:8]
                    date = datetime.datetime.strptime(splitted, "%Y%m%d-%H%M%S")
                    date = date.strftime("%Y:%m:%d 12:00:00")
                    datearray.append(date)
                elif len(splitted) == 19:
                    splitted = splitted[:19]
                    date = datetime.datetime.strptime(splitted, "%Y-%m-%d_%H-%M-%S")
                    date = date.strftime("%Y:%m:%d %H:%M:%S")
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
