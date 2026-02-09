file = open('./data.txt', 'r')

lines = file.readlines()

for line in lines:
    print(line.strip()) # Remove empty new lines

file.close()


with open ('./data.txt', 'r') as file1:
    line = file1.readline()
    print(line)
    