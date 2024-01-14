import numpy as np

# Step 1: Create the input matrix with specified coordinates as 1
input_matrix = np.zeros((8, 8))
input_matrix[2, 2] = 1
input_matrix[2, 4] = 1
input_matrix[4, 2] = 1
input_matrix[4, 4] = 1

# Step 2: Initialize the output matrix with zeros
output_matrix = np.zeros_like(input_matrix)

# Step 3: Define the rotation parameters (center coordinates and angle)
Cx, Cy = 4, 4  # Center of rotation
angle_degrees = 45
angle_radians = np.radians(angle_degrees)

# Loop through each pixel in the output matrix
for y_out in range(output_matrix.shape[0]):
    for x_out in range(output_matrix.shape[1]):
        # Apply rotation transformation
        x_in = int((x_out - Cx) * np.cos(angle_radians) - (y_out - Cy) * np.sin(angle_radians)) + Cx
        y_in = int((x_out - Cx) * np.sin(angle_radians) + (y_out - Cy) * np.cos(angle_radians)) + Cy

        # Copy the pixel value to the output matrix if within bounds
        if 0 <= x_in < input_matrix.shape[1] and 0 <= y_in < input_matrix.shape[0]:
            output_matrix[y_out, x_out] = input_matrix[y_in, x_in]

# Step 4: Print the input and output matrices
print("Input Matrix:")
print(input_matrix)

print("\nOutput Matrix (Rotation):")
print(output_matrix)
