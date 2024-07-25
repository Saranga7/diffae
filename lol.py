import os
import glob
import random
import shutil
from tqdm import tqdm

source_path = '/projects/deepdevpath2/Saranga/Explaining-In-Style-Reproducibility-Study/data/Kaggle_FFHQ_Resized_256px/flickrfaceshq-dataset-nvidia-resized-256px/resized/'
destination_path = '/projects/deepdevpath2/Saranga/diffae/imgs/'

# Ensure the destination path exists
os.makedirs(destination_path, exist_ok=True)

# Get all image files from the source directory
all_images = glob.glob(os.path.join(source_path, '*.jpg'))  # Adjust the file extension if necessary

# Sample 1000 random images
sampled_images = random.sample(all_images, 1000)

# Copy sampled images to the destination directory
for image in tqdm(sampled_images, desc="Copying images"):
    shutil.copy(image, destination_path)

print(len(all_images))

print("Finished copying 1000 images.")
