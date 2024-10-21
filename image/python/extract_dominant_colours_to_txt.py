import os, os.path

import cv2, numpy as np
from sklearn.cluster import KMeans

import json
import csv

from PIL import Image
from PIL.ExifTags import TAGS

# SETTINGS
TARGETFOLDER = 'squared_cropped' # folder with images to extract colors from
NUMBER_OF_COLORS_TO_DETECT = 5 # number of dominant colors to extract
VALID_EXTENSIONS = ('.jpg', '.jpeg', '.png') # valid image extensions


# MAIN
path = './' + TARGETFOLDER + '/'
all_files = os.listdir(path)

image_files = [f for f in all_files if f.lower().endswith(VALID_EXTENSIONS)]

# 

for image_file in image_files:
    # Construct the full image path
    image_path = os.path.join(path, image_file)
    print('processing ', image_path)
    
    # Read the image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    reshape = image.reshape((image.shape[0] * image.shape[1], 3))

    # Calculate n most dominant colors
    cluster = KMeans(n_clusters=NUMBER_OF_COLORS_TO_DETECT).fit(reshape)
    labels = np.arange(0, len(np.unique(cluster.labels_)) + 1)
    (hist, _) = np.histogram(cluster.labels_, bins=labels)
    hist = hist.astype("float")
    hist /= hist.sum()

    # Write the color data to a text file
    txt_file_path = './colors.txt'
    with open(txt_file_path, 'a') as txtfile:
        for color, weight in zip(cluster.cluster_centers_, hist):
            r, g, b = map(int, color)
            txtfile.write(f'{r} {g} {b} {weight}\n')