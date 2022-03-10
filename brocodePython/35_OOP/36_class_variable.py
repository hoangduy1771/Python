class Car:
    # class variables - by default, all instances of this class will have wheels == 4
    wheels = 4

    # constructor
    def __init__(self, make, model, year, color):
        self.make = make  # instance variable
        self.model = model  # instance variable
        self.year = year  # instance variable
        self.color = color  # instance variable


car_no_1 = Car("Mercedes_Benz", "A-Class", "2022", "Polar White")
car_no_2 = Car("Audi", "R8", "2023", "Brilliant Black")

car_no_1.wheels = 6
car_no_2.wheels = 8

print(car_no_1.wheels)
print(car_no_2.wheels)

Car.wheels = 1
print(Car.wheels)
