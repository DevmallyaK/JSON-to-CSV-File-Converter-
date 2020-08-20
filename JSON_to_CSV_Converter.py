import json
import csv

with open('../Sample-JSON-file-with-multiple-records-download.json') as json_file:
    data = json.load(json_file)

emp_data = data['users']

data_file = open('../JSON_to_CSV/output.csv', 'w')

csv_writer = csv.writer(data_file)

count = 0

for emp in emp_data:
    if count == 0:
        header = emp.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(emp.values())

data_file.close()