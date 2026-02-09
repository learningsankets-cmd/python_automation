line_to_write = ['\nline 1,\n', 'line 2']

with open('./new_course/Plain Text Files/test.txt', 'a') as file:
    file.writelines(line_to_write)
