import numpy as np
import cv2

# Load the image
image_path = r'C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\lenna.png'
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Image not found or could not be loaded.")
else:
    # Define the kernel size and standard deviation
    kernel_size = 9
    sigma = 1.0

    # Create a Gaussian kernel
    kernel = np.fromfunction(
        lambda x, y: (1/ (2 * np.pi * sigma ** 2)) * 
                      np.exp(-((x - (kernel_size - 1) / 2) ** 2 + 
                               (y - (kernel_size - 1) / 2) ** 2) / (2 * sigma ** 2)),
        (kernel_size, kernel_size)
    )
    kernel /= np.sum(kernel)

    # Convolve the image with the Gaussian kernel
    blurred_image = cv2.filter2D(image, -1, kernel)

    # Display the original and blurred images
    cv2.imshow("Original Image", image)
    cv2.imshow("Blurred Image", blurred_image)

    # Save the blurred image
    output_path = 'custom_blurred_image.png'
    cv2.imwrite(output_path, blurred_image)

    # Wait for a key press and then close the image windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
