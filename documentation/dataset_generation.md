The dataset used in the ViSAGE-X project is synthetically generated to simulate satellite inspection scenarios.

## RGB Dataset

Base dataset: EuroSAT

- Images converted to grayscale
- Resized to 128×128
- Normal samples: original images
- Anomaly samples: generated using:
  - Crack simulation (line defects)
  - Spot anomalies (localized dark regions)

## Thermal Dataset

Generated synthetically using Python.

### Normal Thermal

- Smooth gradient-based heat distribution
- No abrupt temperature variations

### Thermal Anomaly

- Hotspots (localized high intensity)
- Thermal cracks (linear high-intensity patterns)

## Dataset Composition

- Total samples: 2000
- Normal: 1500
- Anomaly: 500

Each sample contains:
- 1 RGB image
- 1 Thermal image
- 1 Label
