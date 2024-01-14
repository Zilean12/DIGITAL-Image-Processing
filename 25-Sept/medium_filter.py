import cv2
import numpy as np

def median_filter(input_image, kernel_size):
    padding = kernel_size // 2
    height, width = input_image.shape
    output_image = np.zeros((height, width), dtype=np.uint8)

    # Pad the input image
    padded_image = cv2.copyMakeBorder(input_image, padding, padding, padding, padding, cv2.BORDER_CONSTANT)

    for i in range(padding, height + padding):
        for j in range(padding, width + padding):
            neighborhood = padded_image[i - padding:i + padding + 1, j - padding:j + padding + 1]
            sorted_neighborhood = np.sort(neighborhood.flatten())
            median_value = sorted_neighborhood[len(sorted_neighborhood) // 2]
            output_image[i - padding, j - padding] = median_value
    return output_image

# Read the input image
input_image = cv2.imread(r'C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\Lenna.png', cv2.IMREAD_GRAYSCALE)
kernel_size = 3

# Apply the median filter
output_image = median_filter(input_image, kernel_size)
cv2.imshow('Input Image', input_image)
cv2.imshow('Median Filtered Image', output_image)
cv2.imwrite('output_image.jpg', output_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
