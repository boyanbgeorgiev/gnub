import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Function to preprocess an image
def preprocess_image(image_path, target_size=(75, 75)):
    # Load image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error loading image: {image_path}")
        return None
    # Resize image
    resized_image = cv2.resize(image, target_size)
    # Normalize pixel values
    normalized_image = resized_image.astype(np.float32) / 255.0
    # Convert image to grayscale if needed
    # gray_image = cv2.cvtColor(normalized_image, cv2.COLOR_BGR2GRAY)
    return normalized_image

# Directory containing folders for each shark type
root_dir = 'F:/archive (1)/sharks'
output_dir = 'F:/archive (1)/newsharks'

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Loop through folders in the root directory
for folder_name in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder_name)
    if os.path.isdir(folder_path):
        # Create output subdirectory
        output_subdir = os.path.join(output_dir, folder_name)
        os.makedirs(output_subdir, exist_ok=True)
        # Loop through images in the subfolder
        for filename in os.listdir(folder_path):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                # Get image path
                image_path = os.path.join(folder_path, filename)
                # Preprocess image
                preprocessed_image = preprocess_image(image_path)
                if preprocessed_image is not None:
                    # Save preprocessed image
                    output_path = os.path.join(output_subdir, filename)
                    cv2.imwrite(output_path, preprocessed_image * 255)  # Convert back to uint8 for saving

print("Preprocessing complete.")

