import numpy as np

def nearest_neighbor_interpolation(input_matrix, output_shape):
    output_matrix = np.empty(output_shape, dtype=input_matrix.dtype)
    for y_out, x_out in np.ndindex(output_shape):
        y_in = int(y_out * input_matrix.shape[0] / output_matrix.shape[0])
        x_in = int(x_out * input_matrix.shape[1] / output_matrix.shape[1])
        output_matrix[y_out, x_out] = input_matrix[y_in, x_in]
    return output_matrix

if __name__ == "__main__":
    input_matrix = np.random.randint(0, 100, size=(3, 3))
    output_shape = (6, 6)
    interpolated_matrix = nearest_neighbor_interpolation(input_matrix, output_shape)
    print("Input Matrix:")
    print(input_matrix)

    print("\nInterpolated Matrix:")
    for row in interpolated_matrix:
        print(" ".join(map(str, row)))
