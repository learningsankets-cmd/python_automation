# dictionary is key value pairs

customer = {
    "name": "Mario",
    'age': 43,
    'is_verified': True
}

# print(customer['name'])
# none for wrong key or else update default value
# print(customer.get("is_verified1", "False"))


# phone = input("Phone: ")

numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6":  "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}

# for i in phone:
# print(numbers.get(i))


message = input(">")
words = message.split(' ')

emojis = {
    ":)": "🙂",
    ":(": "🙁"
}

output = ''
for word in words:
    output += emojis.get(word, word) + " "


print(output)
