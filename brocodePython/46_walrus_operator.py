# walrus operator := aka assignment expression
#   use to assign variable as a part of a larger expression

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)
# print(foods)

# rewrite the commented code with walrus operator
foods = list()
while (food := input("What is your favorite food?: ")) != "quit":
    foods.append(food)
print(foods)


