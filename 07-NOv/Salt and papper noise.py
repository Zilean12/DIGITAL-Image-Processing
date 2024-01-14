import cv2
import numpy as np

def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = np.copy(image)
    total_pixels = image.size

    # Add salt noise
    num_salt = int(total_pixels * salt_prob)
    salt_coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
    noisy_image[salt_coords] = 1

    # Add pepper noise
    num_pepper = int(total_pixels * pepper_prob)
    pepper_coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape]
    noisy_image[pepper_coords] = 0

    return noisy_image

# Example usage
image = cv2.imread(r"C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\Lenna.png", 0)  # Read a grayscale image
salt_and_pepper_image = add_salt_and_pepper_noise(image, salt_prob=0.01, pepper_prob=0.01)

cv2.imshow('Noisy Image', salt_and_pepper_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
