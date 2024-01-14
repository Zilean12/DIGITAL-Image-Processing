import cv2
import numpy as np

image = cv2.imread(r'C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\Lenna.png')
kernel_size = (5, 5)
height, width, channels = image.shape

# Create an empty output image
smoothed_image = np.zeros_like(image)

# Define the radius of the kernel
kernel_radius_x, kernel_radius_y = kernel_size[0] // 2, kernel_size[1] // 2

# Apply the average filter manually
for y in range(height):
    for x in range(width):
        avg_color = [0, 0, 0]
        count = 0

        for ky in range(-kernel_radius_y, kernel_radius_y + 1):
            for kx in range(-kernel_radius_x, kernel_radius_x + 1):
                pixel_x = x + kx
                pixel_y = y + ky
                if 0 <= pixel_x < width and 0 <= pixel_y < height:
                    avg_color += image[pixel_y, pixel_x]
                    count += 1
        avg_color //= count
        smoothed_image[y, x] = avg_color

cv2.imwrite('smoothed_image.jpg', smoothed_image)
cv2.imshow('Original Image', image)
cv2.imshow('Smoothed Image', smoothed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
