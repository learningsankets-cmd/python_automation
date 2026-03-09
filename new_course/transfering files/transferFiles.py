import csv


def salary_category(salary):
    salary = int(salary)

    if salary < 60000:
        category = 'Average!'
    elif salary >= 60000:
        category = 'GOOD!'
    else:
        category = 'BAD:('

    return category


modified_data = []

with open('./data.csv', 'r') as csv_data:
    csv_reader = csv.reader(csv_data)

    headers = next(csv_reader)

    headers.append('salary_category')

    modified_data.append(headers)
    for row in csv_reader:
        row.append(salary_category(row[4]))

        modified_data.append(row)


with open('./modified_data.csv', 'w', newline='') as csv_modified_data:
    csv_writer = csv.writer(csv_modified_data)
    csv_writer.writerows(modified_data)
