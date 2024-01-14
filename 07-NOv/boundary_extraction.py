import cv2
import numpy as np

def boundary_extraction(image):
    height, width, null= image.shape
    boundary = np.zeros((height, width))

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            # Calculate the gradient using Sobel operators
            dx = int(image[y, x + 1, 0]) - int(image[y, x - 1, 0])
            dy = int(image[y + 1, x, 0]) - int(image[y - 1, x, 0])
            gradient_magnitude = np.sqrt(dx**2 + dy**2)

            # Threshold the gradient magnitude to find edges
            if gradient_magnitude > 100:  # You can adjust this threshold
                boundary[y, x] = 256

    return boundary

image = cv2.imread(r"C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\07-NOv\example3.png")
boundary = boundary_extraction(image)

cv2.imshow("input", image)
cv2.imshow("Boundary", boundary)
cv2.waitKey(0)
cv2.destroyAllWindows()
