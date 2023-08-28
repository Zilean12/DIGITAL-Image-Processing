import numpy as np

def power_law_transform(matrix, gamma, c=1):
    transformed_matrix = c * np.power(matrix, gamma)
    transformed_matrix = np.clip(transformed_matrix, 0, 255)
    return transformed_matrix.astype(np.uint8)

# Generate a random 3x3 matrix with values between 0 and 7
matrix = np.random.randint(0, 8, size=(3, 3))

gamma = 0.5
c = 1

transformed_matrix = power_law_transform(matrix, gamma, c)

print("Original Matrix:")
print(matrix)
print("\nTransformed Matrix:")
print(transformed_matrix)
