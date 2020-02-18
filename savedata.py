import csv

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['CO2', 'NH3', 'TEMP', 'HUM','CO'])
    employee_writer.writerow(['12', '55', '66','55','33'])
