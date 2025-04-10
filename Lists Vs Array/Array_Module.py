import array  # Import the array module

# Step 1: Create an array named 'scores' that stores five test scores (integers)
scores = array.array('i', [85, 90, 88, 92, 87])

# Step 2: Print the third score in the array
print("Third score:", scores[2])  # Output: 88

# Step 3: Change the second score to a new value
scores[1] = 95

# Step 4: Add a new score to the array
scores.append(93)

# Step 5: Print the updated array
print("Updated array:", scores)  # Should show: array('i', [85, 95, 88, 92, 87, 93])
