import pandas as pd

# Task 1: Creating and Manipulating DataFrames.
dict = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

task1_data_frame = pd.DataFrame(dict)
print('----Task1 - create dataframe\n', task1_data_frame)

task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print('----Task1  - add a new column Salary \n', task1_with_salary)

task1_older = task1_with_salary.copy()
task1_older['Age'] += 1
print('----Task1 - modify an existing column Age + 1\n', task1_older)

# Save the DataFrame as a CSV file
task1_older.to_csv('employees.csv', index=False)

# Task 2: Loading Data from CSV and JSON.

# Read data from a CSV file
task2_employees = pd.read_csv('employees.csv')
print(task2_employees)

# just trying different methods
print(task2_employees.describe())
print('Info: \n', task2_employees.info())
print('Columns: \n',task2_employees.columns)

# Load JSON file into a new DataFrame, assigned it to the variable json_employees.
json_employees = pd.read_json('additional_employees.json')
print('----Task2 - loaded JSON:\n', json_employees)

# Combined data - read CSV and JSON
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print('-----Task2 - combined dataframe:\n', more_employees)


# Task 3: Data Inspection - Using Head, Tail, and Info Methods.
# use the head() method
first_three = more_employees.head(3)
print('----Task3 - first three rows\n', first_three)

# use the tail() method
last_two = more_employees.tail(2)
print('----Task3 - last two rows\n', last_two)

# get the shape of a dataframe
employee_shape = more_employees.shape
print('----Task3 - return tuple of rows and columns\n', employee_shape)

# use the info() method
print('----Task3 - info\n',  more_employees.info())

# Task 4: Data Cleaning
dirty_data = pd.read_csv('dirty_data.csv')
print('----Task4 - create dataframe\n', dirty_data)
clean_data = dirty_data.copy()
print('----Task4 - copy\n', clean_data)
# remove dublicated rows and update the existing dataframe
clean_data.drop_duplicates(inplace=True)
print('----Task4 - remove dublicates\n', clean_data)

# convert Age to numeric and handle missing values
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print('----Task4 - convert age to numeric and handle errors\n', clean_data)

# convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
print('----Task4 - convert salary to numeric\n', clean_data)
clean_data['Salary'] = clean_data["Salary"].replace(['unknown', 'n/a'], pd.NA)
print('----Task4 - replace known placeholders (unknown, n/a) with NaN\n', clean_data)

# fill missing numeric values (use fillna).  Fill Age which the mean and Salary with the median

age_mean = clean_data['Age'].mean()
clean_data['Age'] = clean_data['Age'].fillna(age_mean)
median_salary = clean_data['Salary'].median()
clean_data['Salary'] = clean_data['Salary'].fillna(median_salary)
print('----Task4 -  fill missing numeric values \n', clean_data)

# convert Hire Date to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')
print('----Task4 - convert Hire Date to datetime\n', clean_data)

# Strip extra whitespace and standardize Name and Department as uppercase
clean_data['Name'] = clean_data['Name'].str.strip()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print('----Task4 - strip extra whitespace and standardize Name and Department\n', clean_data)