import numpy as np

# Generate a random matrix with values between 0 and 7
matrix = np.random.randint(0, 8, size=(3, 3))

# Parameters for the transformation
c = 2.0  # Scaling factor

# Apply the transformation
transformed_matrix = c * np.log(1 + matrix)

# Convert the transformed matrix elements to integer format
integer_transformed_matrix = transformed_matrix.astype(int)

print("Original Matrix:")
print(matrix)

print("\nTransformed Matrix:")
print(transformed_matrix)

print("\nInteger Transformed Matrix:")
print(integer_transformed_matrix)
