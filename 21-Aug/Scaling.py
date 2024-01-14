import numpy as np

# Create the input matrix with specified coordinates as 1
input_matrix = np.zeros((8, 8))
input_matrix[2, 2] = 1
input_matrix[2, 4] = 1
input_matrix[4, 2] = 1
input_matrix[4, 4] = 1

# Scaling parameters
scale_x = 2
scale_y = 2

# Create scaled indices using a loop
scaled_indices_y = []
scaled_indices_x = []
for i in range(8 * scale_y):
    scaled_indices_y.append(i // scale_y)
for j in range(8 * scale_x):
    scaled_indices_x.append(j // scale_x)

# Apply scaling transformation using a loop
output_matrix_scaling = np.zeros((8 * scale_y, 8 * scale_x))
for i, j in enumerate(scaled_indices_y):
    for k, l in enumerate(scaled_indices_x):
        output_matrix_scaling[i, k] = input_matrix[j, l]

# Input and Output matrices
print("Input Matrix:")
print(input_matrix)

print("\nOutput Matrix (Scaling):")
for row in output_matrix_scaling:
    for val in row:
        print(f"{int(val):^3}", end="")
    print()
