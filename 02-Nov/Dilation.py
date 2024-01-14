import cv2
import matplotlib.pyplot as plt
import numpy as np

img2 = cv2.imread(r"C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\02-Nov\example1.jpeg", 0)

# Acquire the size of the image
p, q = img2.shape

# Define the structuring element (SED)
SED = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
constant1 = 1
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Display the original image on the left
ax1.set_title("Original Image")
ax1.imshow(img2, cmap="gray")

imgDilate = np.zeros((p, q), dtype=np.uint8)

# Dilation operation without using inbuilt CV2 function
for i in range(constant1, p - constant1):
    for j in range(constant1, q - constant1):
        temp = img2[i - constant1:i + constant1 + 1, j - constant1:j + constant1 + 1]
        product = temp * SED
        imgDilate[i, j] = np.max(product)

# Display the dilated image on the right
ax2.set_title("Dilated Image")
ax2.imshow(imgDilate, cmap="gray")

# Display the figure with both images
plt.show()
