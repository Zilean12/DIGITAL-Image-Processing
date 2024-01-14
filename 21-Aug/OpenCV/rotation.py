import numpy as np
import cv2

# Read the image
image = cv2.imread(r"C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\28-Aug\leg.png")

# Get the rotation angle
rotation_angle = int(input("Enter rotation angle (90, 180): "))

# Create the rotation matrix
rotation_matrix = cv2.getRotationMatrix2D((image.shape[1] // 2, image.shape[0] // 2), rotation_angle, 1)

# Rotate the image
rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))

# Display the rotated image
cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
