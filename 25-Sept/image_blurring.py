import numpy as np
import cv2

def gaussian_blur(image, kernel_size, sigma):
    # Create a Gaussian kernel.
    kernel = np.zeros(kernel_size)
    center_x, center_y = kernel_size[0] // 2, kernel_size[1] // 2

    for i in range(kernel_size[0]):
        for j in range(kernel_size[1]):
            x, y = i - center_x, j - center_y
            kernel[i, j] = np.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))

    # Normalize the kernel.
    kernel /= np.sum(kernel)

    # Get the dimensions of the input image
    image_height, image_width, channels = image.shape

    # Initialize the output image
    blurred_image = np.zeros_like(image, dtype=np.float64)

    # Convolve the image with the Gaussian kernel for each channel
    for c in range(channels):
        for i in range(image_height):
            for j in range(image_width):
                # Define the region of interest (ROI) for the convolution
                roi = image[max(i - center_x, 0):min(i + center_x + 1, image_height),
                            max(j - center_y, 0):min(j + center_y + 1, image_width), c]

                # Apply the convolution operation
                blurred_image[i, j, c] = np.sum(kernel[:roi.shape[0], :roi.shape[1]] * roi)

    return blurred_image.astype(np.uint8)

# Example usage:
if __name__ == "__main__":
    input_image = cv2.imread(r'C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\Lenna.png')
    kernel_size = (5, 5)
    sigma = 1.0

    # Apply Gaussian blur to the image
    blurred_image = gaussian_blur(input_image, kernel_size, sigma)

    cv2.imshow('Original Image', input_image)
    cv2.imshow('Blurred Image', blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
