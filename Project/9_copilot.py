Name,Major,GPA,Scholarship
Teri,Math,3.15,No
Sue,Biology,2.75,Yes
Markus,Biology,3.25,Yes
Anders,Math,3.30,No
Leigh,Math,3.57,Yes
Jon,Math,3.67,Yes
Maya,Biology,2.90,Yes
Alex,Math,2.80,No
Nina,Biology,3.40,Yes
Sam,Math,3.00,No
Ravi,Biology,3.10,Yes
Liam,Math,2.95,No
Ella,Biology,3.50,Yes
Omar,Math,3.20,No
Zoe,Biology,2.85,Yes
Ivan,Math,3.60,Yes
Tina,Biology,3.35,Yes
Paul,Math,2.70,No
Sara,Biology,3.45,Yes
Ben,Math,3.55,Yes
import csv

students = {}

with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students[row['Name']] = {
            'Major': row['Major'],
            'GPA': float(row['GPA']),
            'Scholarship': row['Scholarship']
        }

gpas = [info['GPA'] for info in students.values()]
average_gpa = sum(gpas) / len(gpas)
print('Average GPA:', round(average_gpa, 2))

print('Above average students:')
for name, info in students.items():
    if info['GPA'] > average_gpa:
        print(name, info['Major'], info['GPA'])

print('Students who earned a scholarship:')
for name, info in students.items():
    if info['Scholarship'] == 'Yes':
        print(name, info['Major'], info['GPA'])
