import cv2
import numpy as np
# Load the image
img = cv2.imread(r'C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\Lenna.png')
# Generate random Gaussian noise
mean = 0
stddev = 180
noise = np.zeros(img.shape, np.uint8)
cv2.randn(noise, mean, stddev)
# Add noise to image
noisy_img = cv2.add(img, noise)
# Save noisy image
cv2.imwrite('noisy_img.jpg', noisy_img)
