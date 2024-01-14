import numpy as np

# Function for erosion
def erosion(img, SE):
    m, n = img.shape
    imgErode = np.zeros((m, n), dtype=np.uint8)

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            imgErode[i, j] = np.min(img[i - 1:i + 2, j - 1:j + 2] * SE)

    return imgErode

# Function for dilation
def dilation(img, SE):
    m, n = img.shape
    imgDilate = np.zeros((m, n), dtype=np.uint8)

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            imgDilate[i, j] = np.max(img[i - 1:i + 2, j - 1:j + 2] + SE)

    return imgDilate

# Define a sample binary image (0 and 1 values)
img = np.array([[0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0]], dtype=np.uint8)

# Define the structuring element with a kernel size of 3x3
kernel_size = (3, 3)
SE = np.ones(kernel_size, dtype=np.uint8)

# Erode the image
AeB = erosion(img, SE)

# Dilate the eroded image (opening operation)
AoB = dilation(AeB, SE)

# Dilate the opened image followed by erosion (closing operation)
AoBdB = dilation(AoB, SE)
AoBdBeB = erosion(AoBdB, SE)

# Print the results (optional)
print("Original Image:")
print(img)
print("\nEroded Image:")
print(AeB)
print("\nOpened Image:")
print(AoB)
print("\nClosed Image:")
print(AoBdBeB)
