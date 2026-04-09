# ViSAGE-X: Multimodal Edge AI for Satellite Anomaly Detection

ViSAGE-X is a multimodal anomaly detection system designed for satellite inspection using RGB and thermal imagery. The system combines deep learning with edge deployment principles to verify structural anomalies triggered by telemetry signals.

---

## Overview

Satellite systems often rely on telemetry (voltage, temperature, current) to detect irregular behavior. However, telemetry alone cannot confirm physical damage.

ViSAGE-X addresses this by:

- Using telemetry as a trigger
- Performing visual and thermal verification using CNNs
- Running on edge hardware (FPGA)

---

## Key Idea

When a telemetry anomaly is detected:

→ Capture RGB + Thermal data  
→ Feed into CNN-A  
→ Detect structural anomaly  

This ensures anomalies are not just detected, but also **visually verified**.

---

## Dataset

A custom multimodal dataset was created due to lack of publicly available paired RGB + thermal satellite anomaly data.

### Composition

- Total Samples: 2000  
- Normal: 1500  
- Anomaly: 500  

Each sample contains:
- RGB Image (grayscale processed)
- Thermal Image (synthetically generated)
- Label (Normal / Anomaly)

---

## Dataset Generation

### RGB (EuroSAT-based)

- Source: EuroSAT satellite imagery
- Preprocessing:
  - Converted to grayscale
  - Resized to 128×128

### RGB Anomalies

Simulated using:
- Crack-like line defects
- Localized distortions

---

### Thermal Dataset

#### Normal
- Smooth gradient-based heat maps

#### Anomaly
- Hotspots
- Thermal cracks
- Disrupted heat patterns

---

## Multimodal Input

Each input is represented as:
