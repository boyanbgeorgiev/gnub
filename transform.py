import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def preprocess_image(image_path, target_size=(75, 75)):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error loading image: {image_path}")
        return None
    resized_image = cv2.resize(image, target_size)
    normalized_image = resized_image.astype(np.float32) / 255.0
    return normalized_image

root_dir = 'F:/archive (1)/sharks'
output_dir = 'F:/archive (1)/newsharks'

os.makedirs(output_dir, exist_ok=True)

for folder_name in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder_name)
    if os.path.isdir(folder_path):
        output_subdir = os.path.join(output_dir, folder_name)
        os.makedirs(output_subdir, exist_ok=True)
        for filename in os.listdir(folder_path):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                image_path = os.path.join(folder_path, filename)
                preprocessed_image = preprocess_image(image_path)
                if preprocessed_image is not None:
                    output_path = os.path.join(output_subdir, filename)
                    cv2.imwrite(output_path, preprocessed_image * 255) 

print("Preprocessing complete.")

