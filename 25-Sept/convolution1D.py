def convolution_1d(input_signal, kernel):
    # Get the length of the input signal and kernel
    signal_length = len(input_signal)
    kernel_length = len(kernel)
    
    # Initialize the result array with zeros
    result = [0] * (signal_length + kernel_length - 1)
    
    # Flip the kernel
    kernel = kernel[::-1]
    
    # Perform convolution
    for i in range(signal_length):
        for j in range(kernel_length):
            result[i + j] += input_signal[i] * kernel[j]
    
    return result

# Define the input signal and kernel
input_signal = [0, 0, 0, 1, 0, 0, 0]
kernel = [8, 2, 3, 2, 1]

# Perform convolution
result = convolution_1d(input_signal, kernel)

# Print the result
print("Input Signal:", input_signal)
print("Kernel:", kernel)
print("Full Convolution Result:", "without Chropped Convolution Result", result)
