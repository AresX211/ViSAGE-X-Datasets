The system processes both RGB and thermal data simultaneously.

## Input

- Thermal image
- RGB image

## Fusion

Images are combined into a 2-channel tensor:

[Thermal, RGB]

## Purpose

- Capture structural anomalies (RGB)
- Capture thermal anomalies (heat distribution)

## Use Case

Triggered by telemetry anomalies such as:
- Voltage spikes
- Temperature irregularities

The CNN-A model verifies if a physical anomaly exists.
