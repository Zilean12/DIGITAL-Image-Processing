import numpy as np
import matplotlib.pyplot as plt

def matrix_histogram_equalization(matrix):
    # Compute the histogram of the input matrix
    histogram, bins = np.histogram(matrix, bins=256, range=(0, 256))
    
    # Compute the cumulative distribution function (CDF)
    cdf = histogram.cumsum()
    
    # Normalize the CDF to the range [0, 255]
    cdf_normalized = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())
    
    # Round and convert to integer
    cdf_normalized = cdf_normalized.astype('uint8')
    
    # Apply the mapping to the original matrix
    equalized_matrix = cdf_normalized[matrix]
    
    return equalized_matrix

# Create a random 2D matrix for demonstration
np.random.seed(0)
matrix = np.random.randint(0, 30, size=(4, 4), dtype=np.uint8)

# Perform matrix histogram equalization
equalized_matrix = matrix_histogram_equalization(matrix)

# Plot the original matrix, equalized matrix, and histograms side by side
plt.figure(figsize=(16, 8))

# Original matrix
plt.subplot(2, 2, 1)
plt.text(0.5, 0.5, str(matrix), fontsize=12, ha='center', va='center')
plt.title('Original Matrix')
plt.axis('off')

# Equalized matrix
plt.subplot(2, 2, 2)
plt.text(0.5, 0.5, str(equalized_matrix), fontsize=12, ha='center', va='center')
plt.title('Equalized Matrix')
plt.axis('off')

# Original histogram
plt.subplot(2, 2, 3)
plt.hist(matrix.ravel(), bins=256, range=(0, 256), color='blue', alpha=0.7)
plt.title('Original Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# Equalized histogram
plt.subplot(2, 2, 4)
plt.hist(equalized_matrix.ravel(), bins=256, range=(0, 256), color='red', alpha=0.7)
plt.title('Equalized Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
