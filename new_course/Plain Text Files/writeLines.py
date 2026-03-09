line_to_write = ['\nline 1,\n', 'line 2']

with open('./test.txt', 'a') as file:
    file.writelines(line_to_write)


print("Lines are succesfully written in file..", file)
