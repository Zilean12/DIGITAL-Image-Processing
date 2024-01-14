import cv2

# Load the image
image_path = r'C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\lenna.png'
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Image not found or could not be loaded.")
else:
    # Define the kernel size (odd number)
    kernel_size = (5, 5)

    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(image, kernel_size, 0)

    # Display the original and blurred images
    cv2.imshow("Original Image", image)
    cv2.imshow("Blurred Image", blurred_image)

    # Save the blurred image
    output_path = 'blurred_image.png'
    cv2.imwrite(output_path, blurred_image)
    
    # Wait for a key press and then close the image windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
