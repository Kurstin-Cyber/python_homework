import csv
import os
import custom_module
from datetime import datetime



employees = {"fields": [], "rows": []}


def read_employees():
    global employees
    
    file_path = os.path.join(os.path.dirname(__file__), '../csv/employees.csv')
    
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            all_rows = list(reader)
            employees['fields'] = all_rows[0]
            employees['rows'] = all_rows[1:]
    except Exception as e:
        print(f'An exception occured: {e}')
        exit()
    return employees

read_employees()




def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == int(employee_id), employees['rows']))
   return matches

def sort_by_last_name():
    last_name_index = column_index('last_name')
    employees['rows'].sort(key=lambda row: row[last_name_index])
    return employees['rows']



def employee_dict(row):
   
   data_dict = {
        header:value    
        for header, value in zip(employees['fields'], row)
        if header != 'employee_id'
   }

   return data_dict



def column_index(header_name):
    return employees['fields'].index(header_name)

employee_id_column = column_index('employee_id')

first_name_column = column_index('first_name')


def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == int(employee_id)
    
    matches = list(filter(employee_match, employees['rows']))
    return matches



def first_name(row_number):
    return employees['rows'][row_number][first_name_column]

first_name_column = column_index('first_name')


def all_employees_dict():
   return {emp[employee_id_column]: employee_dict(emp) for emp in employees['rows']}



def get_this_value():
    
    return os.getenv('THISVALUE')


def set_that_secret(new_secret):
    
    custom_module.set_secret(new_secret)
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

sort_by_last_name()
print(employees)