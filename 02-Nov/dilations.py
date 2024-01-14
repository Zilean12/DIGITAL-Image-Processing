import cv2
import matplotlib.pyplot as plt

# Read the image for dilation
img = cv2.imread(r"C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\02-Nov\example1.jpeg", 0)

# Define the structuring element (SED)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# Perform dilation using the built-in cv2.dilate function
imgDilate = cv2.dilate(img, kernel)

# Create a figure to display both images side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Display the original image on the left
ax1.set_title("Original Image")
ax1.imshow(img, cmap="gray")

# Display the dilated image on the right
ax2.set_title("Dilated Image")
ax2.imshow(imgDilate, cmap="gray")

# Save the dilated image
cv2.imwrite("Dilated.png", imgDilate)

# Display the figure with both images
plt.show()
