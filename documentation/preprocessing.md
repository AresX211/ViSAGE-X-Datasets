All images undergo the following preprocessing steps:

## Steps

1. Convert RGB to grayscale
2. Resize to 128×128
3. Normalize pixel values:
   - Scale to [0,1]
   - Normalize to [-1,1]

## Output Format

Each sample is converted into a tensor:

(2, 128, 128)

- Channel 0 → Thermal
- Channel 1 → RGB

This format is used as input to the CNN-A model.
