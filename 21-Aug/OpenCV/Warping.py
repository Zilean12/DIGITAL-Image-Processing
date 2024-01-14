import cv2
import numpy as np

def forward_image_warping(image, transformation_matrix):
    h, w = image.shape[:2]
    warped_image = cv2.warpAffine(image, transformation_matrix, (w, h))
    return warped_image

def backward_image_warping(image, transformation_matrix):
    h, w = image.shape[:2]
    inverse_matrix = cv2.invertAffineTransform(transformation_matrix)
    warped_image = cv2.warpAffine(image, inverse_matrix, (w, h))
    return warped_image

# Load an input image
input_image = cv2.imread(r"C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\28-Aug\cameraman.tif")

# Define a transformation matrix
transformation_matrix = np.array([[2, 0, 0],
                                  [0, 2, 0]], dtype=np.float32)

# Ask the user for their choice of warping
warping_choice = input("Enter 'forward' or 'backward' image warping: ")

if warping_choice == 'forward':
    warped_image = forward_image_warping(input_image, transformation_matrix)
    cv2.imshow("Warped Image (Forward)", warped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif warping_choice == 'backward':
    warped_image = backward_image_warping(input_image, transformation_matrix)
    cv2.imshow("Warped Image (Backward)", warped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Invalid choice")
