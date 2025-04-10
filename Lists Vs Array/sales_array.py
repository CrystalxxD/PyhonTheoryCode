import numpy as np  # Import NumPy library

# Step 1: Create a 2D NumPy array to represent sales data for each year
sales_data = np.array([
    [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100],  # 2015 sales data
    [1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1850, 1950, 2050, 2150],  # 2016 sales data
])

# Step 2: Print the sales for the second year (index 1)
print("Sales for 2016:", sales_data[1]) 

# Step 3: Change the sales for July in the first year (2015) to a new value
sales_data[0, 6] = 1650  

# Step 4: Add a new row for another year (2017)
new_year_data = np.array([1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200])
sales_data = np.append(sales_data, [new_year_data], axis=0)

# Step 5: Print the updated sales data
print("Updated sales data:\n", sales_data)
