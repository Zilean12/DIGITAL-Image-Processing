import numpy as np

def generate_random_matrix(rows, cols, min_value, max_value):
    return np.random.randint(min_value, max_value + 1, size=(rows, cols))

def calculate_matrix_negative(matrix, L):
    return (L - 1) - matrix

# Define matrix dimensions and value range
rows = 4
cols = 4
min_value = 0
max_value = 7  
L = 8

# Generate a random matrix
random_matrix = generate_random_matrix(rows, cols, min_value, max_value)

print("Random Matrix:")
print(random_matrix)

# Calculate the matrix negative using the formula
negative_matrix = calculate_matrix_negative(random_matrix, L)

print("\nMatrix Negative:")
print(negative_matrix)
