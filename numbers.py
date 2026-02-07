import math  # to use complex methods for math (Python Docs for more details)


x = 1
x = 1.1
x = 1+2j  # a+bi - complex number


print(10 + 2)
print(10 - 2)
print(10 * 2)
print(10 / 3)  # floating point
print(10 // 3)  # int
print(10 ** 3)  # power
print(10 % 3)

x = 10

x = x+10
x += 90
print(x)


# functions
print(round(2.6))  # neareset int
print(abs(-9))  # absolute int
print(math.ceil(4.4))  # smallest int greter than equal to current value


# More functions
# x = input("x: ")
# print(type(x))
# y = int(x) + 1

# print(f"x: {x}, y: {y}")


# type conversion
# int()
# float()
# bool()
# str()


# Falsy values
# ""
# 0
# None
# bool(0
# ... )
# False
# bool(1)
# True
# bool(-1)
# True
# bool("")
# False
# bool("False")
# True
# bool()
# False

# conditional operators
temperature = 100

if temperature < 57:
    print("Its warm")
    print("Drink water")
elif temperature > 200:
    print("Its not that warm")
else:
    print("Its too warm!")
print("Done")

# ternary operator
age = 23
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)


# logical opereator (and, or, not)
high_income = True
good_credit = False
student = False

if high_income or good_credit:
    print("You can get loan")
else:
    print("you cant get loan")

if not student:
    print("You can get loan")
else:
    print("you cant get loan")


if (high_income or good_credit) and not student:
    print("You can get loan,,,,,")
else:
    print("you cant get loan")


age = 2

if 18 <= age < 65:
    print("eligible")


# loops
# for loop
for number in range(3):
    print("MSG", number)


for num in range(1, 4, 2):
    print(num)


successful = 1
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Failed")


# nested loops
for i in range(5):
    for j in range(3):
        print(f"({i},{j})")

# iterables
# range
print(type(range(5)))

for num in range(4):
    print(num)

# string
for letter in "Hello There":
    print(letter)

# list
for num in [1, 2, 45, 23, 6, 2]:
    print(num)


# while loop

number = 100
while number > 0:
    print(number)
    number //= 2


command = ""

# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

# infinite loop
# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break
count = 0
for i in range(1, 10):
    if i % 2 == 0:
        count += 1
        print(i)

print(f"we have {count} even numbers")


# 1- Perform a task
# functions
def greet():
    print("Hello")
    print("There!")


greet()

# arguments


def greet1(first_name, last_name):
    print(f"Hello There! {first_name} {last_name}")


greet1("John", "Doe")


# 2 - Return a value
def get_greeting(name):
    return f"Hi, {name}"


print(get_greeting("Mario"))

# keyword argument
print(get_greeting(name="Ninja"))


# default argument must come after mandatory parameters
def increment(number, by=1):
    return number+by


print(increment(2, 7))


# xargs


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(1, 2, 3, 45, 9))
