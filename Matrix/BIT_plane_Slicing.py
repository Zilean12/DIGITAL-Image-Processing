import numpy as np

def bit_plane_slice(matrix, num_planes):
    bit_planes = []
    
    for bit_pos in range(num_planes):
        # Create a bitmask for the current bit position
        bitmask = 1 << bit_pos
        
        # Extract the bit-plane by performing a bitwise AND operation
        bit_plane = (matrix & bitmask) >> bit_pos
        
        bit_planes.append(bit_plane)
        
    return bit_planes

# Create a randomly generated matrix
matrix = np.random.randint(0, 8, size=(3, 3))

# Number of bit-planes to extract
num_planes = 3
print("=" * 50)

# Display the original matrix
print("Original Matrix:")
print(matrix)
print("=" * 20)

# Perform bit-plane slicing for the first 3 bit-planes
sliced_planes = bit_plane_slice(matrix, num_planes)

# Display the result
for i, plane in enumerate(sliced_planes):
    plane_type = "LSB" if i == 0 else "Center" if i == 1 else "MSB"
    print(f"{plane_type} Bit-Plane:")
    print(plane)
    print("=" * 20)
