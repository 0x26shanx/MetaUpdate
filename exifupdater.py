from exiftool import ExifToolHelper

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
