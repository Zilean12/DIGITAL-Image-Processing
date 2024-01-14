import numpy as np
import cv2

# Read the image
image = cv2.imread(r"C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\28-Aug\leg.png")

# Scaling parameters
scale_x = 8
scale_y = 8

# Apply scaling transformation using OpenCV
scaled_image = cv2.resize(image, dsize=(8 * scale_y, 8 * scale_x))

# Show the original and scaled images
cv2.imshow("Original Image", image)
cv2.imshow("Scaled Image", scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
    