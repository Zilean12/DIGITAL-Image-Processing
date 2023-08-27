import numpy as np

def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def get_adjacent(matrix, x, y, rows, cols, adjacent_coords):
    valid_adjacent = []
    for i, j in adjacent_coords:
        if is_valid(i, j, rows, cols):
            valid_adjacent.append(((i, j), matrix[i][j]))
    return valid_adjacent

def main():
    rows, cols = 4, 4  # Fixed 4x4 matrix size
    matrix = np.random.randint(0, 100, size=(rows, cols))

    print("Generated Matrix:")
    print(matrix)

    x, y = map(int, input("Enter the row and column index of the element: ").split())
    selected_pixel_value = matrix[x][y]
    print("\nSelected Pixel:")
    print(f"Pixel at ({x}, {y}): {selected_pixel_value}")

    print("\nSelect the type of adjacency:")
    print("1. 4-Adjacent")
    print("2. 8-Adjacent")
    print("3. Mixed-Adjacent")

    choice = int(input("Enter your choice (1/2/3): "))

    adjacent_coords = [(x, y-1), (x-1, y), (x, y+1), (x+1, y)]

    if choice == 2:
        adjacent_coords.extend([(x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)])

    valid_adjacent = get_adjacent(matrix, x, y, rows, cols, adjacent_coords)

    if choice == 3:
        eight_adj_coords = [(x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]
        eight_adj = get_adjacent(matrix, x, y, rows, cols, eight_adj_coords)
        mixed_adj = [adj for adj in valid_adjacent if adj not in eight_adj]
        valid_adjacent = mixed_adj

    print("\nAdjacent coordinates and values:")
    for (i, j), value in valid_adjacent:
        print(f"({i}, {j}): {value}")

if __name__ == "__main__":
    main()
