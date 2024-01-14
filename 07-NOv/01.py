import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function for erosion
def erosion(img, SE):
    m, n = img.shape
    imgErode = np.zeros((m, n))
    
    for i in range(1, m-1):
        for j in range(1, n-1):
            imgErode[i, j] = np.min(img[i-1:i+2, j-1:j+2] * SE)
    
    return imgErode

# Function for dilation
def dilation(img, SE):
    m, n = img.shape
    imgDilate = np.zeros((m, n), dtype=np.uint8)
    
    for i in range(1, m-1):
        for j in range(1, n-1):
            imgDilate[i, j] = np.max(img[i-1:i+2, j-1:j+2] + SE)
    
    return imgDilate

# Load the input image
img = cv2.imread(r"C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\07-NOv\example2.jpeg",0)

# Save a copy of the input image as "finger.png"
cv2.imwrite("finger.png", img)

# Define the structuring element with a kernel size of 3x3
kernel_size = (3, 3)
SE = np.ones(kernel_size, dtype=np.uint8)

# Erode the image
AeB = erosion(img, SE)

# Dilate the eroded image (opening operation)
AoB = dilation(AeB, SE)

# Dilate the opened image followed by erosion (closing operation)
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
