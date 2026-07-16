import csv
import os
import custom_module
import sys
from datetime import datetime


employees = {"fields": [], "rows": []}


def read_employees():
    global employees
    data_dict = {}
    rows_list = []
    
    try:
        with open('../csv/employees.csv', mode='r') as file:
            reader = csv.reader(file)
            fields = next(reader)
            data_dict['fields'] = fields
            for row in reader:

             rows_list.append(row)

            data_dict['rows'] = rows_list
    except Exception as e:
        print(f'Exception: {type(e).__name__}')
        print(f'Exception Details: {e}')
        sys.exit(1)

    return data_dict
print(employees)


employees = read_employees()
employee_id_column = employees['fields'].index('employee_id')
first_name_column = employees['fields'].index('first_name')  

def column_index(header_name):
    return employees['fields'].index(header_name)


def first_name(row_number):
    return employees['rows'][row_number][first_name_column]


def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == int(employee_id)
    
    matches = list(filter(employee_match, employees['rows']))
    return matches



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



def all_employees_dict():
   return {emp[employee_id_column]: employee_dict(emp) for emp in employees['rows']}



def get_this_value():
    
    return os.getenv('THISVALUE')


def set_that_secret(new_secret):
    
    return custom_module.set_secret(new_secret)
    

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
    global minutes_list
    minutes_list.sort( key=lambda x: x[1])
    formatted_data = [(item[0], item[1].strftime('%B %d, %Y')) for item in minutes_list]

    
    with open('./minutes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(minutes1['fields'])
        writer.writerows(formatted_data)

    return formatted_data

if __name__ == '__main__':
    print('Employees:\n', employees)
    print('Minutes Set:\n', minutes_set)
    print('Minutes List:\n', minutes_list)

sorted_minutes = write_sorted_list()
print('Sorted Minutes List:\n', sorted_minutes)

sort_by_last_name()
print('Sorted Employees:\n', employees)