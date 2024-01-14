def spatial_correlation(signal, filter):
    signal_len = len(signal)
    filter_len = len(filter)
    result_len = signal_len + filter_len - 1
    result = [0] * result_len

    for i in range(result_len):
        for j in range(filter_len):
            if i - j >= 0 and i - j < signal_len:
                result[i] += signal[i - j] * filter[j]

    return result

# Define the input signal and the filter
signal = [0, 0, 0, 1, 0, 0, 0]
filter = [1, 2, 3, 2, 8]

# Calculate the spatial correlation
correlation_result = spatial_correlation(signal, filter)

# Print the result
print("Input Signal:", signal)
print("Filter:", filter)
print("Spatial Correlation Result:", correlation_result)
