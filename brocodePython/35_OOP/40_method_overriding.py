# overriding = ability of OOP to allow subclass to provide a specific implementation of a method in parent class
class Animal:

    def eat(self):
        print("This animal is eating")


class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating")


rabbit = Rabbit()
rabbit.eat()
