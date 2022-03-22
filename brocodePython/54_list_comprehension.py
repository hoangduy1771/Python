# list comprehension = a way to create a new list with less syntax
#                      can mimic a certain lambda functions, easier to read
#
#                      list comprehension formula for creating a list:
#                      If you just want a list:
#                       list = [expression for the item in iterable]
#
#                      If you have a conditional you want to check, add conditional at the end:
#                       list = [expression for the item in iterable if condition]
#
#                      if you need to use if/else, add if/else after expression
#                       list = [expression (if/else) for the item in iterable]

squares = []                    # create an empty list
for i in range(1, 11):          # create a for loop
    squares.append(i * i)       # define what each loop iteration should do
print(squares)

# rewrite above function with list comprehension
squares = [i * i for i in range(1, 11)]
print(squares)

# mimic lambda function
students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = list(filter(lambda x: x >= 60, students))

print(passed_students)

# rewrite above function with list comprehension to mimic lambda function
passed_students = [x for x in students if x >= 60]
result_students = [x if x >= 60 else "FAILED" for x in students]
print(passed_students)
print(result_students)












