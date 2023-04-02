from exiftool import ExifToolHelper

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