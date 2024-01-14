import cv2
import numpy as np

image = cv2.imread(r'C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\lenna.png', cv2.IMREAD_GRAYSCALE)
sobelx = cv2.Sobel(image, cv2.CV_32F, 1, 0, ksize=5)
sobely = cv2.Sobel(image, cv2.CV_32F, 0, 1, ksize=5)

# Calculate the magnitude of gradients
gradient_magnitude = np.sqrt(sobelx ** 2 + sobely ** 2)

gradient_magnitude = np.uint8(255 * gradient_magnitude / np.max(gradient_magnitude))
cv2.imshow('Gradient Magnitude', gradient_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()
