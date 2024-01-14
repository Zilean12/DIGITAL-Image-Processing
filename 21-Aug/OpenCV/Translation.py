import numpy as np
import cv2
import matplotlib.pyplot as plt

# Read the image file
image = cv2.imread(r"C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\28-Aug\leg.png")

# Create a translation matrix and convert it to the correct data type
translation_matrix = np.array([[1, 0, 2], [0, 1, -1]], dtype=np.float32)

# Apply the translation to the image
translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))

# Save the output image
cv2.imwrite('translated_image.jpg', translated_image)

# Display the original and translated images
plt.subplot(121)
plt.imshow(image)
plt.title('Original Image')
plt.subplot(122)
plt.imshow(translated_image)
plt.title('Translated Image')
plt.show()
