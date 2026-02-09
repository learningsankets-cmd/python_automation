# Open file  (reading mode)
file = open('./data.txt', 'r')

# Read whole file

contents = file.read()

print(contents)


# closing the file to save resources
file.close()


