import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread(r"C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\03-Sept\lenna.png", cv2.IMREAD_GRAYSCALE)

# Apply histogram equalization
equalized_image = cv2.equalizeHist(image)

# Create a figure with two rows and two columns
plt.figure(figsize=(12, 8))

# Plot the original image
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

# Plot the histogram for the original image
plt.subplot(2, 2, 2)
plt.hist(image.ravel(), 256, [0, 256], color='blue')
plt.title('Original Image Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# Plot the equalized image
plt.subplot(2, 2, 3)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')

# Plot the histogram for the equalized image
plt.subplot(2, 2, 4)
plt.hist(equalized_image.ravel(), 256, [0, 256], color='green')
plt.title('Equalized Image Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# Adjust spacing between subplots
plt.tight_layout()

# Show the plots
plt.show()
