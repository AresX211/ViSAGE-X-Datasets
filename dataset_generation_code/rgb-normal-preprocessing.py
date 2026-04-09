from PIL import Image
import numpy as np
import os

rgb_selected_path = r"E:\ViSAGE\Datasets\Cnn A\rgb\selected\eurosat_normal"
rgb_processed_path = r"E:\ViSAGE\Datasets\Cnn A\rgb\processed_normal"

os.makedirs(rgb_processed_path, exist_ok=True)

for file in os.listdir(rgb_selected_path):
    img_path = os.path.join(rgb_selected_path, file)
    
    img = Image.open(img_path)
    
    # Convert to grayscale
    img = img.convert("L")
    
    # Resize to 128x128
    img = img.resize((128, 128))
    
    # Save
    img.save(os.path.join(rgb_processed_path, file))

print("RGB preprocessing complete.")
