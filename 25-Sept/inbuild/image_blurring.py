import cv2
import numpy as np

# Load the image.
image = cv2.imread(r"C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\Lenna.png")
smoothed_image = np.copy(image)

# Apply a 3x3 kernel blur
cv2.blur(image, (3, 3), smoothed_image)
cv2.imshow("Blurred Image with 3x3 Kernel", smoothed_image)
smoothed_image = np.copy(image)
cv2.GaussianBlur(image, (5, 5), 1.5, smoothed_image)
cv2.imshow("Blurred Image with 5x5 Kernel and Sigma = 1.5", smoothed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
