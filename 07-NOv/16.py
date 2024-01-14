import cv2
import numpy as np

# Load the image
img = cv2.imread(r'C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\02-Nov\example.jpeg',0)

# Define a structuring element for erosion and dilation with a kernel size of 3
kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]])

# Perform erosion on the original image
def custom_erosion(image, kernel):
    eroded_image = np.zeros(image)
    kernel_size = kernel.shape[0]
    padding_size = kernel_size // 2

    for i in range(padding_size, image.shape[0] - padding_size):
        for j in range(padding_size, image.shape[1] - padding_size):
            roi = image[i - padding_size:i + padding_size + 1, j - padding_size:j + padding_size + 1]
            min_value = np.min(roi)
            eroded_image[i, j] = min_value
    return eroded_image

# Perform dilation on the eroded image
def custom_dilation(image, kernel):
    dilated_image = np.zeros_like(image)
    kernel_size = kernel.shape[0]
    padding_size = kernel_size // 2

    for i in range(padding_size, image.shape[0] - padding_size):
        for j in range(padding_size, image.shape[1] - padding_size):
            roi = image[i - padding_size:i + padding_size + 1, j - padding_size:j + padding_size + 1]
            max_value = np.max(roi)
            dilated_image[i, j] = max_value
    return dilated_image

# Perform boundary extraction
def custom_boundary_extraction(image, eroded_image):
    boundary = image - eroded_image
    return boundary

# # Apply an average filter to the original image
# def custom_average_filter(image, kernel):
#     filtered_image = np.zeros_like(image)
#     kernel_size = kernel.shape[0]
#     padding_size = kernel_size // 2
#     for i in range(padding_size, image.shape[0] - padding_size):
#         for j in range(padding_size, image.shape[1] - padding_size):
#             roi = image[i - padding_size:i + padding_size + 1, j - padding_size:j + padding_size + 1]
#             average_value = np.mean(roi)
#             filtered_image[i, j] = average_value
#     return filtered_image

# Perform erosion on the filtered image
eroded_image = custom_erosion(img, kernel)

# Perform dilation on the eroded image
dilated_image = custom_dilation(eroded_image, kernel)

# Perform boundary extraction
boundary_image = custom_boundary_extraction(img, eroded_image)

# Display the original, filtered, eroded, dilated, and boundary images
cv2.imshow("Input Image", img)
# cv2.imshow("Filtered Image", filtered_image)
cv2.imshow("Eroded Image", eroded_image)
cv2.imshow("Dilated Image", dilated_image)
cv2.imshow("Boundary Image", boundary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
