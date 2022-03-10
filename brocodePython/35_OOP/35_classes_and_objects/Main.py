from classes import Car, MotorBike

car_1 = Car("Toyota", "Fortuner", "2022", "Black")
print(car_1.make)
print(car_1.model)
car_1.drive()
car_1.stop()

car_2 = Car("Ford", "Everest", "2023", "Black Mica")
print(car_2.make)
print(car_2.model)
car_2.drive()
car_2.stop()

#  ===================================================

MyMotorBike = MotorBike()
MyMotorBike.make = "BMW"
MyMotorBike.model = "R Nine T"
MyMotorBike.year = "2022"
MyMotorBike.color = "Black"

# print(MyMotorBike.make)
