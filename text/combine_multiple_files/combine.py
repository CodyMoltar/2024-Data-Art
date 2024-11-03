# this script combines multiple text files into one text file.

# we need to import the os module, so we can list the files in a directory
import os

# we define the source folder
SOURCE_FOLDER = '../data/new-media-student-diary/'

# we define the output file
OUTPUT_FILE = './combined.txt'

# we open the output file in write mode
with open(OUTPUT_FILE, 'w') as output_file:
    # we loop through all the files in the source folder
    for file in os.listdir(SOURCE_FOLDER):
        # we check if the file is a text file
        if file.endswith('.txt'):
            # we open the file in read mode
            with open(SOURCE_FOLDER + file, 'r') as input_file:
                # we read the content of the file
                text = input_file.read()
                # we write the content of the file to the output file
                output_file.write(text)