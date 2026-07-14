import csv
import os
import custom_module
from datetime import datetime
employees = None

employee_id_column = None

def read_employees():
    global employees


    employee_dict = {"fields": [], "rows": []}

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '..', 'csv', 'employees.csv')

    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)

            employee_dict["fields"] = header
            employee_dict["rows"] = list(reader)

            employees = employee_dict
            return employees
        
    except Exception as e:
        print(f"An error occurred: {e}")
        employees = employee_dict
        return employee_dict



def column_index(column_name):
   
   return employees["fields"].index(column_name)


read_employees()
employee_id_column = column_index("employee_id")

if __name__ == "__main__":
    
    print(f"Employee ID column index is: {employee_id_column}")


def first_name(row_number):
    first_name_index = column_index("first_name")

    row_data = employees["rows"][row_number]

    name = row_data[first_name_index]

    return name

print(first_name(0))


def employee_find(employee_id):
    
    def employee_match(row): 
         
        return int(row[employee_id_column]) == employee_id
    
    matches = list(filter(employee_match, employees['rows']))

    return matches

print(employee_find(4))

def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees['rows']))

    return matches


def sort_by_last_name():
    last_index = column_index("last_name")
    employees['rows'].sort(key=lambda row: row[last_index])

    return employees['rows']



def employee_dict(row):
    return {header: value for header, value in zip(employees['fields'], row)
            if header != "employee_id"}

if __name__ == "__main__":
    sample_row = employees["rows"][0]
    print(employee_dict(sample_row))


def all_employees_dict(employees=None):
    if employees is None:
        employees = globals().get('employees')

    result = {}

    for row in employees['rows']:
        emp_data = employee_dict(row)

        emp_id = row[employee_id_column]

        result[emp_id] = emp_data
    
    return result



def get_this_value():
    
    return"ABC"

if __name__ == "__main__":
    
    value = get_this_value()

    print(f"The environment variable THISVALUE is: {value}")


def set_that_secret(new_secret):
    print(f"The secret is: {custom_module.secret}")

    custom_module.set_secret('swordfish')
    print(f"The updated secret is: {custom_module.secret}")
    

def get_minutes_data(filepath):
    with open(filepath, 'r') as file:
        reader = csv.reader(file)

        fields = next(reader)

        rows = [tuple(row) for row in reader]

    return {"fields": fields, "rows": rows}

def read_minutes():
    minutes1 = get_minutes_data('../csv/minutes1.csv')
    minutes2 = get_minutes_data('../csv/minutes2.csv')
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()

print("Minutes 1:", minutes1)
print("Minutes 2:", minutes2)


def create_minutes_set():
    set1 = set(minutes1['rows'])
    set2 = set(minutes2['rows'])

    return set1.union(set2)
minutes_set = create_minutes_set()

print("Minutes Set:", minutes_set)

def create_minutes_list():
    minutes_list_raw = list(minutes_set)

    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1],"%B %d, %Y")), minutes_list_raw))
    return minutes_list

minutes_list = create_minutes_list()

print("Minutes List:", minutes_list)

def write_sorted_list():
    sorted_data = sorted(minutes_list, key=lambda x: x[1])

    formatted_data = [(item[0], item[1].strftime("%B %d, %Y"))
                      for item in sorted_data]
    with open('./minutes.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(minutes1['fields'])

        writer.writerows(formatted_data)

    return formatted_data

sorted_minutes = write_sorted_list()

print('Sorted Minutes List', sorted_minutes)