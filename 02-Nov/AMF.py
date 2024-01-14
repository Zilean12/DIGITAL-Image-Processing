import cv2

# Load the input image
input_image = cv2.imread(r'C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\Lenna.png')

# Set the kernel size and other parameters for the adaptive median filter
kernel_size = 5  # Adjust this based on your requirements
max_diameter = 9  # Maximum filter size
sigma_color = 50  # Adjust this based on your requirements
sigma_space = 50  # Adjust this based on your requirements

# Apply the adaptive median filter
output_image = cv2.adaptiveBilateralFilter(input_image, (kernel_size, kernel_size), sigma_color, sigma_space, max_diameter)

# Save the filtered image
cv2.imwrite('output.jpg', output_image)

# Display the original and filtered images (optional)
cv2.imshow('Original Image', input_image)
cv2.imshow('Filtered Image', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
