import cv2
import numpy as np

# Read the input binary image
image = cv2.imread(r"C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\07-NOv\example2.jpeg", cv2.IMREAD_GRAYSCALE)

# Create a kernel for morphological operations
kernel = np.ones((5, 5), np.uint8)

# Perform morphological closing to fill holes in objects
filled_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Save the filled image
cv2.imwrite('output_image.png', filled_image)
