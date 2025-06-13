import numpy as np
import time

# Create a 1000x1000 matrix with random numbers
matrix = np.random.rand(1000, 1000)

# Measure execution time for row sum
start_row = time.time()
row_sum = np.sum(matrix, axis=1)
end_row = time.time()
row_time = end_row - start_row

# Measure execution time for column sum
start_col = time.time()
column_sum = np.sum(matrix, axis=0)
end_col = time.time()
col_time = end_col - start_col

# Report the execution times
print(f"Row sum execution time: {row_time:.6f} seconds")
print(f"Column sum execution time: {col_time:.6f} seconds")
