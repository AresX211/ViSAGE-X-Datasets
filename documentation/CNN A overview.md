# CNN-A Model Overview

CNN-A is a dual-branch convolutional neural network designed for multimodal anomaly detection.

## Architecture

- Thermal branch (CNN)
- RGB branch (CNN)
- Feature fusion layer
- Fully connected classifier

## Output

Binary classification:
- 0 → Normal
- 1 → Anomaly

## Performance

- Accuracy: ~99.8%
- Robust to INT8 quantization

## Deployment Target

- FPGA (PYNQ-Z2)
- Edge AI system
