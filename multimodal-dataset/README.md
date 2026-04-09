This folder contains representative samples from the ViSAGE-X multimodal anomaly dataset.

Each sample consists of:

- Left: Thermal Image (heatmap visualization)
- Right: RGB Image (grayscale)

- **Normal**: No structural or thermal anomaly
- **Anomaly**: Contains simulated defects such as:
  - Cracks
  - Surface distortions
  - Thermal hotspots

- Thermal images are displayed using a heatmap colormap for better interpretability.
- Underlying data is grayscale intensity-based.
- Each sample corresponds to a paired RGB and thermal input used for CNN-A training.

These samples demonstrate the multimodal fusion approach used in the anomaly detection pipeline.
