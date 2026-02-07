class Animal:
    def walk(self):
        print("Animal Waliking")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog()
dog.walk()
