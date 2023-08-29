import numpy as np
import cv2
import matplotlib.pyplot as plt

# Read the image in greyscale
image = cv2.imread(r'C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\28-Aug\leg.png', 0)
width = image.shape[0]
height = image.shape[1]

#Iterate over each pixel and change pixel value to binary using np.binary_repr() and store it in a list.
binary_pixel_list = []
for i in range(width):
    for j in range(height):
        binary_pixel_list.append(np.binary_repr(image[i][j], width=8)) # width = no. of bits


# We have a list of strings where each string represents binary pixel value. To extract bit planes we need to iterate over the strings and store the characters corresponding to bit planes into lists.
# Multiply with 2^(n-1) and reshape to reconstruct the bit image.
bit0_img = (np.array([int(pixel[7]) for pixel in binary_pixel_list], dtype=np.uint8)*255).reshape(width, height)
bit1_img = (np.array([int(pixel[6]) for pixel in binary_pixel_list], dtype=np.uint8)*255).reshape(width, height)
bit2_img = (np.array([int(pixel[5]) for pixel in binary_pixel_list], dtype=np.uint8)*255).reshape(width, height)
bit3_img = (np.array([int(pixel[4]) for pixel in binary_pixel_list], dtype=np.uint8)*255).reshape(width, height)
bit4_img = (np.array([int(pixel[3]) for pixel in binary_pixel_list], dtype=np.uint8)*255).reshape(width, height)
bit5_img = (np.array([int(pixel[2]) for pixel in binary_pixel_list], dtype=np.uint8)*255).reshape(width, height)
bit6_img = (np.array([int(pixel[1]) for pixel in binary_pixel_list], dtype=np.uint8)*255).reshape(width, height)
bit7_img = (np.array([int(pixel[0]) for pixel in binary_pixel_list], dtype=np.uint8)*255).reshape(width, height)


bit0_img = cv2.cvtColor(bit0_img, cv2.COLOR_BGR2RGB)
bit1_img = cv2.cvtColor(bit1_img, cv2.COLOR_BGR2RGB)
bit2_img = cv2.cvtColor(bit2_img, cv2.COLOR_BGR2RGB)
bit3_img = cv2.cvtColor(bit3_img, cv2.COLOR_BGR2RGB)
bit4_img = cv2.cvtColor(bit4_img, cv2.COLOR_BGR2RGB)
bit5_img = cv2.cvtColor(bit5_img, cv2.COLOR_BGR2RGB)
bit6_img = cv2.cvtColor(bit6_img, cv2.COLOR_BGR2RGB)
bit7_img = cv2.cvtColor(bit7_img, cv2.COLOR_BGR2RGB)

 
plt.subplot(121), plt.imshow(bit0_img), plt.title("bit0")
plt.subplot(122), plt.imshow(bit1_img), plt.title("bit1")
plt.show()
plt.subplot(121), plt.imshow(bit2_img), plt.title("bit2")
plt.subplot(122), plt.imshow(bit3_img), plt.title("bit3")
plt.show()
plt.subplot(121), plt.imshow(bit4_img), plt.title("bit4")
plt.subplot(122), plt.imshow(bit5_img), plt.title("bit5")
plt.show()
plt.subplot(121), plt.imshow(bit6_img), plt.title("bit6")
plt.subplot(122), plt.imshow(bit7_img), plt.title("bit7")
plt.show()