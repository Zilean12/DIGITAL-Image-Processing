import numpy as np

def binary_threshold(matrix, threshold):
    # Create a binary mask where values above or equal to the threshold become 1, and others become 0
    binary_matrix = np.where(matrix >= threshold, 1, 0)
    return binary_matrix

# Example matrix
matrix = np.array([[4, 3, 5, 2],
                   [3, 6, 4, 6],
                   [2, 2, 6, 5],
                   [7, 6, 4, 1]])

# Set the threshold value
threshold = 4

# Apply binary thresholding
binary_result = binary_threshold(matrix, threshold)

print("Original Matrix:")
print(matrix)
print("\nThresholded Matrix:")
print(binary_result)
