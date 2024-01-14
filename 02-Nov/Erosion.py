import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image for erosion
img1 = cv2.imread(r"C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\02-Nov\example1.jpeg", 0)

# Acquire size of the image
m, n = img1.shape

# Define the structuring element
k = 3  # Adjust the kernel size as needed
SE = np.ones((k, k))
constant = (k - 1) // 2

# Define a new image for erosion
imgErode = np.zeros((m, n))

# Erosion without using inbuilt cv2 function
for i in range(constant, m - constant):
    for j in range(constant, n - constant):
        temp = img1[i - constant : i + constant + 1, j - constant : j + constant + 1]
        product = temp * SE
        imgErode[i, j] = np.max(product)

# Show the original image
plt.figure(figsize=(8, 4))
plt.subplot(121)
plt.imshow(img1, cmap="gray")
plt.title("Original Image")

# Show the eroded image
plt.subplot(122)
plt.imshow(imgErode, cmap="gray")
plt.title("Eroded Image")



# Save the eroded image
cv2.imwrite("Eroded.png", imgErode)

plt.show()
