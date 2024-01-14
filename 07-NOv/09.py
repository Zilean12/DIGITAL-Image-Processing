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

# Custom function for erosion
def custom_erosion(image, kernel):
    height, width = image.shape
    result = np.zeros((height, width), dtype=np.uint8)

    k_height, k_width = kernel.shape

    for y in range(height):
        for x in range(width):
            min_val = 255

            for ky in range(k_height):
                for kx in range(k_width):
                    img_y = y + ky - k_height // 2
                    img_x = x + kx - k_width // 2

                    if 0 <= img_y < height and 0 <= img_x < width:
                        min_val = min(min_val, image[img_y, img_x])

            result[y, x] = min_val

    return result

# Custom function for dilation
def custom_dilation(image, kernel):
    height, width = image.shape
    result = np.zeros((height, width), dtype=np.uint8)

    k_height, k_width = kernel.shape

    for y in range(height):
        for x in range(width):
            max_val = 0

            for ky in range(k_height):
                for kx in range(k_width):
                    img_y = y + ky - k_height // 2
                    img_x = x + kx - k_width // 2

                    if 0 <= img_y < height and 0 <= img_x < width:
                        max_val = max(max_val, image[img_y, img_x])

            result[y, x] = max_val

    return result

# Load the input image
image = cv2.imread(r"C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\07-NOv\example3.png")
boundary = boundary_extraction(image)
filled_image = fill_holes(boundary)

# Create a combined image by placing the boundary, filled_image, and the original image side by side
combined_image = np.hstack((boundary, filled_image))
original_image = cv2.imread(r"C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\07-NOv\example3.png", cv2.IMREAD_GRAYSCALE)

# Create a kernel for custom erosion and dilation
kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]], dtype=np.uint8)

# Apply custom morphological operations to the original image
opened_image = custom_dilation(custom_erosion(original_image, kernel), kernel)
closed_image = custom_erosion(custom_dilation(opened_image, kernel), kernel)

# Display the combined image, original image, and custom morphological operations results using matplotlib
plt.figure(figsize=(16, 8))

# Combined Image
plt.subplot(131), plt.imshow(combined_image, cmap='gray'), plt.title('Combined Image')

# Original Image
plt.subplot(132), plt.imshow(original_image, cmap='gray'), plt.title('Original Image')

# Custom Morphological Operations
plt.subplot(133)
plt.imshow(closed_image, cmap='gray')
plt.title("C((O(A,B),B)")

plt.tight_layout()
plt.show()
