import csv

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

