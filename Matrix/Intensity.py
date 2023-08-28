import numpy as np

def custom_intensity_mapping(matrix):
    result_matrix = np.copy(matrix)  # Create a copy of the input matrix

    # Iterate through each element in the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            r = matrix[i, j]  # Original pixel intensity

            # Apply the custom mapping
            if 3 <= r <= 5:
                result_matrix[i, j] = 7
            else:
                result_matrix[i, j] = 0

    return result_matrix

# Given matrix
matrix = np.array([[4, 3, 5, 2],
                   [3, 6, 4, 6],
                   [2, 2, 6, 5],
                   [7, 6, 4, 1]])

output_matrix = custom_intensity_mapping(matrix)

print("Input Matrix:")
print(matrix)

print("\nIntensity - level Slicing:")
print(output_matrix)
