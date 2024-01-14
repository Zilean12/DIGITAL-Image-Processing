import numpy as np

# Generate two random matrices
matrix_a = np.random.randint(0, 40, size=(3, 3))
matrix_b = np.random.randint(0, 40, size=(3, 3))

print("Matrix A:\n", matrix_a)
print("Matrix B:\n", matrix_b)

operation = input("Select an operation (1: Add, 2: Subtract, 3: Multiply): ")

if operation not in ["1", "2", "3"]:
    print("Invalid operation.")
    exit()

# Perform the operation
if operation == "1":
    operation = "Addition"
    result = matrix_a + matrix_b

elif operation == "2":
    operation = "Subtraction"
    result = matrix_a - matrix_b

elif operation == "3": 
    operation = "Multiplication"
    result = np.dot(matrix_a, matrix_b)

# Print the result
print(f"\nResult of {operation}:\n{result}")
