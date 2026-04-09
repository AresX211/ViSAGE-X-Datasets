import numpy as np
import cv2
import os
import random

thermal_normal_path = r"E:\ViSAGE\Datasets\Cnn A\thermal\normal"

os.makedirs(thermal_normal_path, exist_ok=True)

def generate_normal_thermal(size=128):
    # Base smooth gradient
    x = np.linspace(0, 1, size)
    y = np.linspace(0, 1, size)
    xv, yv = np.meshgrid(x, y)

    base = 0.5 + 0.2 * xv + 0.1 * yv

    # Add small smooth variation
    noise = np.random.normal(0, 0.02, (size, size))

    thermal = base + noise
    thermal = np.clip(thermal, 0, 1)

    return (thermal * 255).astype(np.uint8)

# Generate 1500 normal thermal images
for i in range(1500):
    img = generate_normal_thermal()
    filename = os.path.join(thermal_normal_path, f"thermal_normal_{i}.png")
    cv2.imwrite(filename, img)

print("Normal thermal dataset created.")
