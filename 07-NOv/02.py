import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function for erosion
def erosion(img, SE):
    imgErode = cv2.erode(img, SE, iterations=1)
    return imgErode

# Function for dilation
def dilation(img, SE):
    imgDilate = cv2.dilate(img, SE, iterations=1)
    return imgDilate

# Load the input image
img = cv2.imread(r"C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\07-NOv\example2.jpeg", 0)

# Save a copy of the input image as "finger.png"
cv2.imwrite("finger.png", img)

# Define the structuring element using an inbuilt OpenCV function
SE = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# Erode the image
AeB = erosion(img, SE)

# Dilate the eroded image. This gives opening operation
AoB = dilation(AeB, SE)

# Dilate the opened image followed by erosion. This will give closing of the opened image
AoBdB = dilation(AoB, SE)
AoBdBeB = erosion(AoBdB, SE)

# Plot all the images
plt.figure(figsize=(10, 10))

plt.subplot(3, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original")

plt.subplot(3, 2, 2)
plt.title("E(A,B)")
plt.imshow(AeB, cmap='gray')

plt.subplot(3, 2, 3)
plt.title("O(A, B)")
plt.imshow(AoB, cmap='gray')

plt.subplot(3, 2, 4)
plt.title("D(O(A,B), B)")
plt.imshow(AoBdB, cmap='gray')

plt.subplot(3, 2, 5)
plt.title("C((O(A,B),B),B)")
plt.imshow(AoBdBeB, cmap='gray')

# Save the filtered image
cv2.imwrite("finger_filtered.png", AoBdBeB)

# Display the plots
plt.show()
