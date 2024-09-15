import os, os.path

import cv2, numpy as np
from sklearn.cluster import KMeans

import json
import csv



# SETTINGS
TARGETFOLDER = 'squared_cropped' # folder with images to extract colors from
NUMBER_OF_COLORS_TO_DETECT = 5 # number of dominant colors to extract
VALID_EXTENSIONS = ('.jpg', '.jpeg', '.png') # valid image extensions


# MAIN
path = './' + TARGETFOLDER + '/'
all_files = os.listdir(path)

image_files = [f for f in all_files if f.lower().endswith(VALID_EXTENSIONS)]

data = {}

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

    image_info = {
        'dominant_colors': cluster.cluster_centers_.tolist(),
        'weights': hist.tolist()
    }

    data[image_file] = image_info # Add to the same list [x, x]

# print(data)

with open('./data_' + TARGETFOLDER + '.json', 'w') as outfile:
    json.dump(data, outfile, indent=4, default=lambda x: x.tolist() if isinstance(x, np.ndarray) else x)


# Write the data to a CSV file
csv_file_path = './data_' + TARGETFOLDER + '.csv'
with open(csv_file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write the header
    header = ['filename']
    for i in range(NUMBER_OF_COLORS_TO_DETECT):
        header.append(f'colour_{i+1}')
        header.append(f'weight_{i+1}')
    csv_writer.writerow(header)
    
    # Write the data rows
    for filename, info in data.items():
        row = [filename]
        for color, weight in zip(info['dominant_colors'], info['weights']):
            row.append(color)
            row.append(weight)
        csv_writer.writerow(row)