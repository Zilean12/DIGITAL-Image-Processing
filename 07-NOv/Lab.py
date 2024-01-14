import cv2
import numpy as np

img = cv2.imread(r'C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\Lenna.png', 0)

# Salt and Pepper Noise
salt_prob = 0.01
pepper_prob = 0.01
noisy_img = img.copy()

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        rand = np.random.rand()
        if rand < salt_prob:
            noisy_img[i, j] = 255  # Salt noise
        elif rand > 1 - pepper_prob:
            noisy_img[i, j] = 0  # Pepper noise

# Median filter
def median_filter(img, kernel_size):
    padding = kernel_size // 2
    height, width = img.shape
    output = np.zeros((height, width), dtype=np.uint8)
    PaddedImage = cv2.copyMakeBorder(img, padding, padding, padding, padding, cv2.BORDER_CONSTANT)
    for i in range(padding, height + padding):
        for j in range(padding, width + padding):
            N = PaddedImage[i - padding:i + padding + 1, j - padding:j + padding + 1]
            median_value = np.median(N)
            output[i - padding, j - padding] = median_value
    return output

# Arithmetic Mean filter
def arithmetic_mean_filter(img, kernel_size):
    padding = kernel_size // 2
    height, width = img.shape
    output = np.zeros((height, width), dtype=np.uint8)
    PaddedImage = cv2.copyMakeBorder(img, padding, padding, padding, padding, cv2.BORDER_CONSTANT)
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size ** 2)
    for i in range(padding, height + padding):
        for j in range(padding, width + padding):
            N = PaddedImage[i - padding:i + padding + 1, j - padding:j + padding + 1]
            output[i - padding, j - padding] = np.sum(N)
    return output

kernel_size = 3 
filtered_img_median = median_filter(noisy_img, kernel_size)
arithmetic_mean = arithmetic_mean_filter(noisy_img, kernel_size)


cv2.imshow("Input", img)
cv2.imshow("Noise", noisy_img)
cv2.imshow("Median Filter", filtered_img_median)
cv2.imshow("Arithmetic Mean Filter", arithmetic_mean)
cv2.waitKey(0)
cv2.destroyAllWindows