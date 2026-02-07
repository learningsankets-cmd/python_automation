class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(12, 45)
print(point1.x)
point1.draw()
point1.move()


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("Talking")


person1 = Person("mario")
print("Hello There", person1.name.capitalize())
person1.talk()



class Animal:
    def walk(self):
        print("Animal Waliking")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog()
dog.walk()
