# str.format()

animal = "cow"
item = "moon"

print("The {} jump over the {}.".format(animal, item))
print("The {1} jump over the {0}.".format(animal, item))
print("The {animal_1} jump over the {item_1}.".format(animal_1="cow", item_1="moon"))

text = "The {} jump over the {}."
print(text.format(animal, item))

# ========================================================================================

name = "Duy"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:<10}. Nice to meet you".format(name))  # left align (can't visual, its the default)
print("Hello, my name is {:>10}. Nice to meet you".format(name))  # right align the name variable
print("Hello, my name is {:^10}. Nice to meet you".format(name))  # center the name variable

# =========================================================================================

number = 3.14159
number_1 = 1000000
print("The pi number is: {:0.2f}".format(number))
print("The number_1 is: {:,}".format(number_1))

# display number_1 in binary form
print("The number_1 is: {:b}".format(number_1))
# display number_1 in octo number
print("The number_1 is: {:o}".format(number_1))
# display number_1 in hexadecimal
print("The number_1 is: {:x}".format(number_1))  # lowercase
print("The number_1 is: {:X}".format(number_1))  # uppercase
