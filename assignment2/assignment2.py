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
