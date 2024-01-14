import cv2 as cv
import numpy as np

def calculate_median(array):
    sorted_array = np.sort(array)
    median = sorted_array[len(array) // 2]
    return median

def stage_A(pixel_value, neighborhood, initial_window, max_window):
    S_xy = initial_window
    S_max = max_window

    target = neighborhood.flatten()
    z_min = np.min(target)
    z_max = np.max(target)
    z_med = calculate_median(target)

    if z_min < z_med < z_max:
        return stage_B(pixel_value, z_min, z_med, z_max)
    else:
        S_xy += 2
        if S_xy <= S_max:
            return stage_A(pixel_value, neighborhood, S_xy, S_max)
        else:
            return z_med

def stage_B(pixel_value, z_min, z_med, z_max):
    if z_min < pixel_value < z_max:
        return pixel_value
    else:
        return z_med

def adaptive_median_filter_image(input_image, initial_window, S_max):
    xlen, ylen = input_image.shape
    output_image = input_image.copy()

    for row in range(initial_window, xlen - initial_window - 1):
        for col in range(initial_window, ylen - initial_window - 1):
            neighborhood = input_image[row - initial_window: row + initial_window + 1,
                           col - initial_window: col + initial_window + 1]
            new_intensity = stage_A(input_image[row, col], neighborhood, initial_window, S_max)
            output_image[row, col] = new_intensity

    return output_image

def main():
    original_image = cv.imread(r"C:\Users\aryan\OneDrive - st.niituniversity.in\DIP\Lenna.png", cv.IMREAD_GRAYSCALE)
    cv.imshow("Original Image", original_image)

    noise = np.random.normal(0, 1, original_image.size)
    noise = noise.reshape(original_image.shape).astype("uint8")
    noisy_image = cv.add(original_image, noise)
    cv.imshow("Noisy Image", noisy_image)

    filtered_image = adaptive_median_filter_image(noisy_image, initial_window=3, S_max=5)
    cv.imshow("Adaptive Median Filtered Image", filtered_image)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
