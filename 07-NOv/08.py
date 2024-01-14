import cv2
import numpy as np
import matplotlib.pyplot as plt

def boundary_extraction(image):
    height, width, _ = image.shape
    boundary = np.zeros((height, width), dtype=np.uint8)

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            # Calculate the gradient using Sobel operators
            dx = int(image[y, x + 1, 0]) - int(image[y, x - 1, 0])
            dy = int(image[y + 1, x, 0]) - int(image[y - 1, x, 0])
            gradient_magnitude = np.sqrt(dx**2 + dy**2)

            # Threshold the gradient magnitude to find edges
            if gradient_magnitude > 100:  # You can adjust this threshold
                boundary[y, x] = 255

    return boundary

def fill_holes(image):
    # Find connected components
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(image, connectivity=4)

    # Create an output image
    output_image = np.zeros_like(image)

    # Loop through connected components and fill holes
    for label in range(1, num_labels):
        component_mask = (labels == label).astype(np.uint8) * 255

        # Find contours of the component
        contours, _ = cv2.findContours(component_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Fill the component using fillPoly
        cv2.fillPoly(output_image, contours, 255)

    return output_image

image = cv2.imread(r"C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\07-NOv\example3.png")
boundary = boundary_extraction(image)
filled_image = fill_holes(boundary)

# Create a combined image by placing the boundary and filled_image side by side
combined_image = np.hstack((boundary, filled_image))

# Display the original image, boundary extraction, hole filling, and the combined image using matplotlib
plt.figure(figsize=(16, 8))

# Original Image
plt.subplot(141), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cmap='gray'), plt.title('Original Image')

# Boundary Extraction
plt.subplot(142), plt.imshow(boundary, cmap='gray'), plt.title('Boundary Extraction')

# Hole Filling
plt.subplot(143), plt.imshow(filled_image, cmap='gray'), plt.title('Hole Filling')

plt.tight_layout()
plt.show()

