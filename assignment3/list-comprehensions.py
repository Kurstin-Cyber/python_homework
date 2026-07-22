import csv


file_path = '../csv/employees.csv'

with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    rows = list(reader)
    

full_names = [f'{row[0]} {row[1]}' for row in rows[1:]]
print('Full Names List:', full_names)


e_names = [name for name in full_names if 'e' in name.lower()]
print('Filtered Names:', e_names)