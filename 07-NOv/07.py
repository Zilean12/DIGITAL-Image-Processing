import cv2
import numpy as np

# Read the input binary image
image = cv2.imread(r"C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\07-NOv\example3.png", cv2.IMREAD_GRAYSCALE)

# Threshold the image to create a binary mask
ret, binary_mask = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

# Find connected components manually
def dfs(label, x, y):
    if x < 0 or x >= height or y < 0 or y >= width:
        return
    if labels[x, y] != 0 or binary_mask[x, y] == 0:
        return
    labels[x, y] = label
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        dfs(label, x + dx, y + dy)

height, width = binary_mask.shape
labels = np.zeros_like(binary_mask, dtype=np.int32)
label_count = 0

for x in range(height):
    for y in range(width):
        if binary_mask[x, y] == 255 and labels[x, y] == 0:
            label_count += 1
            dfs(label_count, x, y)

# Create an output image
output_image = np.zeros_like(image)

# Loop through connected components and fill holes
for label in range(1, label_count + 1):
    component_mask = (labels == label).astype(np.uint8) * 255
    
    # Find contours of the component
    contours, _ = cv2.findContours(component_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Fill the component using fillPoly
    cv2.fillPoly(output_image, contours, 255)

# Display the filled image
cv2.imshow('Output Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the filled image
cv2.imwrite('output_image.png', output_image)
