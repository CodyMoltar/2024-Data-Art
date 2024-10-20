import PIL.Image as Image


# open an image
image = Image.open('./squared_cropped/IMG_20210805_213127.png')

# extract EXIF data
exif_data = image._getexif()

# print EXIF data
print(exif_data)