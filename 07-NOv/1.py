import cv2
import numpy as np

# Load the image
img = cv2.imread(r'C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\02-Nov\example.jpeg', cv2.IMREAD_GRAYSCALE)

# Define the kernel
kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]], dtype=np.uint8)

# Perform erosion on the filtered image
def custom_erosion(image, kernel):
    filtered_image = np.zeros_like(image)
    kernel_size = kernel.shape[0]
    padding_size = kernel_size // 2
    for i in range(padding_size, image.shape[0] - padding_size):
        for j in range(padding_size, image.shape[1] - padding_size):
            roi = image[i - padding_size:i + padding_size + 1, j - padding_size:j + padding_size + 1]
            min_value = np.min(roi)
            filtered_image[i, j] = min_value
    return filtered_image

# Apply custom erosion
eroded_image = custom_erosion(img, kernel)

# Display the eroded image
cv2.imshow('Eroded Image', eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
