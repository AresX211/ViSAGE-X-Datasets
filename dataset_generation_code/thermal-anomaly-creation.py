thermal_anomaly_path = r"E:\ViSAGE\Datasets\Cnn A\thermal\anomaly"
os.makedirs(thermal_anomaly_path, exist_ok=True)

def add_hotspot(image):
    size = image.shape[0]
    cx = random.randint(20, size-20)
    cy = random.randint(20, size-20)
    radius = random.randint(5, 15)

    y, x = np.ogrid[:size, :size]
    mask = (x - cx)**2 + (y - cy)**2 <= radius**2
    image[mask] = np.minimum(image[mask] + random.randint(40, 80), 255)

    return image

# Generate 500 anomaly images
for i in range(500):
    img = generate_normal_thermal()
    img = add_hotspot(img)
    filename = os.path.join(thermal_anomaly_path, f"thermal_anomaly_{i}.png")
    cv2.imwrite(filename, img)

print("Thermal anomaly dataset created.")
