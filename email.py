import csv
with open('D:\\temp\\email\\1\\emails2.csv', 'r') as f:
    reader = csv.reader(f)
    print(type(reader))

    i = 0;   
    for row in reader:
        i=i+1
        filename = str(i) + '.eml'
        with open(filename, 'w') as file_object:
            print(row[1])
            file_object.write(row[1])