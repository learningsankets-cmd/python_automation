import csv

with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    for row in csv_reader:
        name = row[1]
        age = row[2]
        city = row[3]
        salary = row[4]
        print(f'"{name}" | "{age}" | "{city}" | "{salary}"')
