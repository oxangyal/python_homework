import csv
import os
import custom_module

def read_employees():
    dict1 = dict({})

    try:
        with open('../csv/employees.csv', 'r') as csvfile:
            lines = csv.reader(csvfile)
            rows = []
            first_line = True
            for line in lines:
                if first_line:
                    dict1['fields'] = line
                    first_line = False
                else:
                    rows.append(line)
            dict1['rows'] = rows
            return dict1
    except Exception as e:
        print(e)

employees = read_employees()
print(employees)
print('Task2:\n', employees)

def column_index(column_name):
    return employees['fields'].index(column_name)
employee_id_column = column_index('employee_id')
print('Task3:\n', f'Employee_id_column: {employee_id_column}')

def  first_name(row_number):
        first_name_idx = column_index('first_name')
        return employees['rows'][row_number][first_name_idx]
print('Task4:\n', first_name(10))

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches
print('Task5:\n', employee_find(4))

def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches
print('Task6:\n', employee_find_2(4))

def sort_by_last_name():
    last_name_index = column_index('last_name')
    employees['rows'].sort(key = lambda row : row[last_name_index])
    return employees['rows']
print('Task7:\n', sort_by_last_name())

def employee_dict(row):
    keys = employees["fields"]
    return dict(zip(keys[1:], row[1:]))

print('Task 8:\n', employee_dict(employees['rows'][0]))

def all_employees_dict():
    employees_dict = {}
    for row in employees['rows']:
            id = row[0]
            employees_dict[id] = employee_dict(row)
    return employees_dict
print('Task 9:\n', all_employees_dict())

def get_this_value():
    return os.getenv('THISVALUE')
print('Task 10:\n', get_this_value())

def set_that_secret(secret):
    custom_module.set_secret(secret)
set_that_secret("hello")
print('Task 11:\n', custom_module.secret)

def read_csv_file(file_path):
    result = {}
    rows = []
    try:
        with open(file_path, 'r') as csvfile:
            lines = csv.reader(csvfile)
            first_line = True
            for line in lines:
                if first_line:
                    result['fields'] = line
                    first_line = False
                else:
                    rows.append(tuple(line))
            result['rows'] = rows
        return result
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return {'fields': [], 'rows': []}
    
def read_minutes():
    minutes1 = read_csv_file('../csv/minutes1.csv')
    minutes2 = read_csv_file('../csv/minutes2.csv')
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print("Task 12:\n Minutes_1:", minutes1)
print("=========================")
print("Task 12:\n Minutes_2:", minutes2)

def create_minutes_set():
    return set(minutes1['rows']).union(set(minutes2['rows']))
minutes_set = create_minutes_set()
print("Task 13:\n", minutes_set)

from datetime import datetime
def create_minutes_list():
    minutes_list = list(minutes_set)
    converted_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    return converted_list
minutes_list = create_minutes_list()
print('Task14:\n', minutes_list)

def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    converted_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))
    with open('./minutes.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(minutes1['fields'])
            for row in converted_list:
                writer.writerow(row)
    return converted_list
print('Task15:\n', write_sorted_list())