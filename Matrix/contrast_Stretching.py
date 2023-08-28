def contrast_stretching(matrix, S1, S2, R1, R2):
    output_matrix = []
    for row in matrix:
        output_row = []
        for pixel in row:
            if pixel < R1:
                output_pixel = S1
            elif pixel > R2:
                output_pixel = S2
            else:
                output_pixel = int(((pixel - R1) / (R2 - R1)) * (S2 - S1) + S1)
            output_row.append(output_pixel)
        output_matrix.append(output_row)
    return output_matrix


# Define the matrix and parameters
matrix = [[4, 3, 5, 2],
          [3, 6, 4, 6],
          [2, 2, 6, 5],
          [7, 6, 4, 1]]
S1 = 2
S2 = 6
R1 = 3
R2 = 5

# Apply contrast stretching
result = contrast_stretching(matrix, S1, S2, R1, R2)

# Print the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)
    
# Print the result
print("\nContrast Stretched Matrix:")
for row in result:
    print(row)