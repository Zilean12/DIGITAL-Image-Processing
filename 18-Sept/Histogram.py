import cv2
import numpy as np
import matplotlib.pyplot as plt

# Input image
image_path = r'C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\lenna.png'
img = cv2.imread(image_path, 0)

# OpenCV
histr_cv2 = cv2.calcHist([img], [0], None, [256], [0, 256])

# Custom method
histogram_custom = np.zeros(256, dtype=np.int32)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        histogram_custom[img[i, j]] += 1

# Plot both histograms in separate subplots
fig, axs = plt.subplots(2)

# plotting using OpenCV
axs[0].plot(histr_cv2)
axs[0].set_title('Histogram (OpenCV)')
axs[0].set_xlabel('Pixel Value')
axs[0].set_ylabel('Frequency')

# plotting using Custom method
axs[1].plot(histogram_custom)
axs[1].set_title('Customized Histogram')
axs[1].set_xlabel('Pixel Value')
axs[1].set_ylabel('Frequency')

plt.tight_layout()
plt.show()
