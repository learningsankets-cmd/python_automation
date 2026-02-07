# x = 1

# print(x)
# s = 1

# print("Hello")

# Variables
students_count = 1000  # integer
rating = 4.99  # float
is_good = True  # boolean
course = "Python"  # string
# print(students_count)


#  String

course = "Python"
meassage = """
This is for
multiline
string
"""

# string functions
len(course)  # Length

# print(course[4])

# print(course[0:3])
# print(course[0:])
# print(course[:3])
# print(course[:])


name = 'Mario"s Ninja'  # Escape character after
# print(name)

firstName = "     John"
lastName = "Doe"

# fullName = firstName + lastName

fullName = f"{firstName} {lastName}"  # Formatted-string
print(fullName.upper())
print(fullName.strip())  # removes whitespace r and l for two sides
print(fullName.find("J"))  # index
print(fullName.replace("D", "g"))
print("goe" in fullName)  # true or fasle
print("isn" not in fullName)  # true or fasle
