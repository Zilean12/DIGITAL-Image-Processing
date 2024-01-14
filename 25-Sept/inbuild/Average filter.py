import cv2
import numpy as np

# Load an image
image = cv2.imread(r'C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\Lenna.png')

# Define the kernel size for the average filter (e.g., 5x5)
kernel_size = (5, 5)

# Apply the average filter using cv2.blur()
smoothed_image = cv2.blur(image, kernel_size)

# Save the smoothed image
cv2.imwrite('smoothed_image.jpg', smoothed_image)

# Display the original and smoothed images
cv2.imshow('Original Image', image)
cv2.imshow('Smoothed Image', smoothed_image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
