# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 10:40:28 2024

@author: VGabor
"""
import os
import csv
from PIL import Image
import numpy as np

# Directory containing the images
image_dir = 'G:/Blender_3D/Chlorophyceae/render_output_SOK7'

# CSV file to store the results
csv_file = 'G:/Blender_3D/Chlorophyceae/render_output_SOK5/results_all_5.csv'

# Open the CSV file for writing
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(["image_path", "name", "tilt", "angle", "white_count", "black_count", "total_pixels", "max_black_x","max_black_y"])

    # Process all images in the directory
    for filename in os.listdir(image_dir):
        if filename.endswith('.jpg'):
            image_path = os.path.join(image_dir, filename)
            image = Image.open(image_path)

            # Convert the image to grayscale
            image = image.convert('L')

            # Convert the grayscale image to binary
            threshold = 128
            image = image.point(lambda p: p > threshold and 255)
            image = image.convert('1')

            # Convert the image data to a numpy array
            image_data = np.array(image)

            # Count the number of white and black pixels
            white_count = np.sum(image_data == True)
            black_count = np.sum(image_data == False)
            total_pixels = image_data.size

            # Find the x-coordinate with the maximum number of black pixels
            black_counts_per_column = np.sum(image_data == False, axis=0)
            max_black_x = np.count_nonzero(black_counts_per_column>0)
            black_counts_per_row = np.sum(image_data == 0, axis=1)
            max_black_y = np.count_nonzero(black_counts_per_row>0)

            parts = filename.split("_")
            part1 = "_".join(parts[:2])  # Euastrum_verrucosum
            part2 = parts[3]  # 90
            part3 = parts[4].split(".")[0]  # 300

            # Write the results to the CSV file
            writer.writerow([image_path, part1, part2, part3, white_count, black_count, total_pixels,max_black_x,max_black_y])
        print(filename)
print("The pixel counts have been written to 'results_all.csv'.")
