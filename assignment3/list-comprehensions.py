import csv


file_path = '../csv/employees.csv'

with open(file_path, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)

full_names = [f'{row[1]} {row[2]}' for row in data[1:]]
print('Full Names List:')
print(full_names)

e_names = [name for name in full_names if 'e' in name.lower()]
print("\nNames containing the letter 'e':")
print(e_names)