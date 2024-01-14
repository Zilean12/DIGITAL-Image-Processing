import cv2
import numpy as np

# Read the image
image = cv2.imread(r'C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\12.png')

# Define the kernel size for median filtering
ksize = 3

# Apply the median filter
smoothed_image = cv2.medianBlur(image, ksize)


# Display the original and filtered images
cv2.imshow("Original Image", image)
cv2.imshow("Median Filtered Image", smoothed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
