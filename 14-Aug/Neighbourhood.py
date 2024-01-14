import numpy as np

def get_neighborhood(matrix, row, col, neighbors):
    neighborhood = []
    directions = {'N4': [(1, 0), (0, 1), (-1, 0), (0, -1)],
                  'Nd': [(1, 1), (-1, -1), (-1, 1), (1, -1)],
                  'N8': [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]}
    for direction in neighbors:
        for dr, dc in directions[direction]:
            r, c = row + dr, col + dc
            if 'N4' in direction and abs(dr) + abs(dc) != 1:
                continue
            if 0 <= r < matrix.shape[0] and 0 <= c < matrix.shape[1]:
                neighborhood.append(matrix[r, c])
    return neighborhood

matrix = np.random.randint(0, 100, size=(5, 5))
print("Generated Matrix:\n", matrix)

selected_row = int(input("Enter the row of the selected pixel: "))
selected_col = int(input("Enter the column of the selected pixel: "))
neighbors_option = input("Choose neighbors (N4, N8, Nd): ").split()

neighborhood = get_neighborhood(matrix, selected_row, selected_col, neighbors_option)
selected_pixel = matrix[selected_row, selected_col]

print("Selected Pixel:", selected_pixel)
print("Selected Neighbors:", neighborhood)
