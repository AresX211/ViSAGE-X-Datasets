import os
import random
import numpy as np
import cv2

rgb_normal_path = r"E:\ViSAGE\Datasets\Cnn A\rgb\processed_normal"
rgb_anomaly_path = r"E:\ViSAGE\Datasets\Cnn A\rgb\processed_anomaly"

os.makedirs(rgb_anomaly_path, exist_ok=True)

all_images = os.listdir(rgb_normal_path)

# Select 600 random images for anomaly generation
selected_images = random.sample(all_images, 600)

def add_occlusion(img):
    h, w = img.shape
    occ_w = random.randint(15, 40)
    occ_h = random.randint(15, 40)
    x = random.randint(0, w - occ_w)
    y = random.randint(0, h - occ_h)

    color = random.randint(0, 80)  # dark occlusion
    img[y:y+occ_h, x:x+occ_w] = color
    return img

def add_crack(img):
    h, w = img.shape
    x1 = random.randint(0, w)
    y1 = random.randint(0, h)
    x2 = random.randint(0, w)
    y2 = random.randint(0, h)

    thickness = 1
    color = random.randint(180, 255)  # bright crack
    cv2.line(img, (x1, y1), (x2, y2), color, thickness)
    return img

# Shuffle for distribution
random.shuffle(selected_images)

both_count = 20
half = 290  # approx half of remaining

for i, file in enumerate(selected_images):
    img_path = os.path.join(rgb_normal_path, file)
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    if i < both_count:
        img = add_occlusion(img)
        img = add_crack(img)

    elif i < both_count + half:
        img = add_occlusion(img)

    else:
        img = add_crack(img)

    save_path = os.path.join(rgb_anomaly_path, f"anomaly_{file}")
    cv2.imwrite(save_path, img)

print("RGB anomaly generation complete.")
