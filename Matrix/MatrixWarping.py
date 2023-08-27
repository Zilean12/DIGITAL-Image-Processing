import numpy as np

def forward_matrix_warping(matrix, transformation_matrix):
    warped_matrix = np.dot(transformation_matrix, matrix)
    return warped_matrix

def backward_matrix_warping(matrix, transformation_matrix):
    warped_matrix = np.dot(np.linalg.inv(transformation_matrix), matrix)
    return warped_matrix

input_matrix = np.array([[1, 2],
                         [3, 4]])

# Define a transformation matrix
transformation_matrix = np.array([[2, 0],
                                  [0, 2]])

# Ask the user for their choice of warping
warping_choice = input("Enter 'forward' or 'backward' matrix warping: ")

if warping_choice == 'forward':
    warped_matrix = forward_matrix_warping(input_matrix, transformation_matrix)
    print("Warped Matrix (Forward):\n", warped_matrix)
elif warping_choice == 'backward':
    warped_matrix = backward_matrix_warping(input_matrix, transformation_matrix)
    print("Warped Matrix (Backward):\n", warped_matrix)
else:
    print("Invalid choice")
