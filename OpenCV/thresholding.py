import cv2

# Read the image
image = cv2.imread(r'C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\28-Aug\note.png', cv2.IMREAD_GRAYSCALE)

# Apply thresholding
threshold_value = 128
max_value = 255
_, thresholded_image = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_BINARY)

# Display the original and thresholded images
cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
