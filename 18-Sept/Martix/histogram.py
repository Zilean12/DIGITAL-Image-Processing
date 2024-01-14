import numpy as np
import matplotlib.pyplot as plt

# Generate a random matrix (you can replace this with your own matrix)
matrix = np.random.randint(0, 25, size=(4, 4), dtype=np.uint8)

# Calculate the histogram
hist, bins = np.histogram(matrix, bins=256, range=(0, 256))

# Create a histogram plot
plt.figure(figsize=(8, 6))
plt.title("Matrix Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.bar(bins[:-1], hist, width=1)
plt.xlim(0, 255)

# Show the histogram
plt.show()
