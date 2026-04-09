import os
import matplotlib.pyplot as plt

# Create Dataset 
dataset = CNNADataset()

print("Total samples:", len(dataset))

# Create Save Directory
save_folder = r"E:\ViSAGE\Multimodal_Samples"
os.makedirs(save_folder, exist_ok=True)

# Generate and Save Samples
num_samples = 20  # you can increase this if needed

for i in range(num_samples):

    x, label = dataset[i]

    # Ensure CPU tensor
    x = x.cpu()

    # Extract channels
    thermal = x[0].numpy()
    rgb = x[1].numpy()

    # Plot figure
    plt.figure(figsize=(6,3))

    # Thermal (heatmap for better interpretation)
    plt.subplot(1,2,1)
    plt.imshow(thermal, cmap='hot')
    plt.title("Thermal")
    plt.axis('off')

    # RGB (grayscale)
    plt.subplot(1,2,2)
    plt.imshow(rgb, cmap='gray')
    plt.title("RGB")
    plt.axis('off')

    # Label
    label_text = "Anomaly" if label == 1 else "Normal"
    plt.suptitle(f"Label: {label_text}")

    plt.tight_layout()

    # Save image
    filename = f"sample_{i}_{label_text}.png"
    plt.savefig(os.path.join(save_folder, filename), dpi=300)

    plt.close()

print("✅ Multimodal samples generated and saved successfully.")
