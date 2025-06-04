# Task 3: List Comprehensions Practice

import pandas as pd

df = pd.read_csv('../csv/employees.csv')

# Create a list of employee names using a list comprehension
employee_names = [f"{row['first_name']} {row['last_name']}" for index, row in df.iterrows()]

# Print the list of employee names
print("All Employee Names:")
print(employee_names)

# Create a filtered list of names containing the letter "e"
names_with_e = [name for name in employee_names if 'e' in name]

print("\nNames Containing 'e':")
print(names_with_e)