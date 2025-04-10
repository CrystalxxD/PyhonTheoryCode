# Step 1: Create a nested list named 'grades'
grades = [
    [85, 90, 88],  # Student 1's grades: Math, Science, English
    [78, 82, 85],  # Student 2's grades: Math, Science, English
    [92, 89, 91]   # Student 3's grades: Math, Science, English
]

# Step 2: Print the grades of the second student
print("Second student's grades:", grades[1])  # Output: [78, 82, 85]

# Step 3: Change the Math grade of the first student
grades[0][0] = 90 

# Step 4: Add a new student with grades
grades.append([88, 93, 87])  

# Step 5: Print the updated list
print("Updated grades list:", grades)
