import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image for erosion
img = cv2.imread(r"C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\02-Nov\example.jpeg", 0)

# Define the structuring element
k = 5  # Adjust the kernel size as needed
kernel = np.ones((k, k), dtype=np.uint8)

# Perform erosion using cv2.erode
imgErode = cv2.erode(img, kernel, iterations=1)

# Display the original and eroded images
plt.figure(figsize=(8, 4))
plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.title("Original Image")

plt.subplot(122)
plt.imshow(imgErode, cmap="gray")
plt.title("Eroded Image")

plt.show()

# Save the eroded image
cv2.imwrite("Eroded_OpenCV.png", imgErode)
