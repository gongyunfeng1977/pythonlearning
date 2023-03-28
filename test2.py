import csv
with open('D:\\temp\\email\\1\\emails2.csv', 'r') as f:
    reader = csv.reader(f)
    print(type(reader))