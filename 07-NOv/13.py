import cv2
import numpy as np

# Load the image
img = cv2.imread(r'C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\02-Nov\example1.jpeg', cv2.IMREAD_GRAYSCALE)

# Generate random Gaussian noise without using built-in functions
mean = 0
stddev = 25  # You can adjust the standard deviation to control the noise intensity
noise = np.random.randn(img.shape[0], img.shape[1]) * stddev
noisy_img = img + noise

# Ensure the noisy image values are within the valid pixel range (0-255)
noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)

# Define a structuring element for erosion and dilation with a kernel size of 3
kernel = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]], dtype=np.uint8)

# Perform erosion on the noisy image
def custom_erosion(image, kernel):
    eroded_image = np.zeros_like(image)
    kernel_size = kernel.shape[0]
    padding_size = kernel_size // 2
    for i in range(padding_size, image.shape[0] - padding_size):
        for j in range(padding_size, image.shape[1] - padding_size):
            roi = image[i - padding_size:i + padding_size + 1, j - padding_size:j + padding_size + 1]
            min_value = np.min(roi)
            eroded_image[i, j] = min_value
    return eroded_image

eroded_image = custom_erosion(noisy_img, kernel)

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

dilated_image = custom_dilation(eroded_image, kernel)

# Display the original, noisy, eroded, and dilated images
cv2.imshow("Input Image", img)
cv2.imshow("Noisy Image", noisy_img)
cv2.imshow("Eroded Image", eroded_image)
cv2.imshow("Dilated Image", dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
