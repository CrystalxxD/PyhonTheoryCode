import numpy as np  # Import NumPy library

# Step 1: Create a 2D NumPy array named 'matrix' with 3 rows and 3 columns of numbers
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Step 2: Print the entire second row
print("Second row:", matrix[1])  # Output: [4, 5, 6]

# Step 3: Change the value in the first row, second column
matrix[0, 1] = 20  

# Step 4: Add a new row to the matrix
new_row = np.array([10, 11, 12])
matrix = np.append(matrix, [new_row], axis=0)

# Step 5: Print the updated matrix
print("Updated matrix:\n", matrix)