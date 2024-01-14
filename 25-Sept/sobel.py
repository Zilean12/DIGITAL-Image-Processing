import cv2
import numpy as np

image = cv2.imread(r'C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\lenna.png', cv2.IMREAD_GRAYSCALE)

# Define Sobel kernels for X and Y directions
sobel_kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_kernel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# Initialize empty arrays for gradient in X and Y directions
sobelx = np.zeros_like(image, dtype=np.float32)
sobely = np.zeros_like(image, dtype=np.float32)

# Iterate through the image to apply Sobel operators manually
for y in range(1, image.shape[0] - 1):
    for x in range(1, image.shape[1] - 1):
        sobelx[y, x] = np.sum(image[y - 1:y + 2, x - 1:x + 2] * sobel_kernel_x)
        sobely[y, x] = np.sum(image[y - 1:y + 2, x - 1:x + 2] * sobel_kernel_y)

# Calculate the magnitude of gradients
gradient_magnitude = np.sqrt(sobelx ** 2 + sobely ** 2)

# Normalize and convert to integers
gradient_magnitude = np.uint8(255 * gradient_magnitude / np.max(gradient_magnitude))

# Create a larger image by concatenating the original and gradient magnitude images horizontally
concatenated_image = np.hstack((image, gradient_magnitude))
cv2.imshow('Original and Gradient Magnitude', concatenated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
