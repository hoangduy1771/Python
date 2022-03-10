class Car:
    # constructor
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This car " + self.model + " is driving")

    def stop(self):
        print("This car " + self.model + " is stopped")


# define a class without using constructor
class MotorBike:
    make = None
    model = None
    year = None
    color = None
