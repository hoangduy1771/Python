# function = block of code which is executed only when it is called

# Example 1:
# def hello():
#     name = input("What is your name? ")
#     age = str(input("How old are you? "))
#     print("Hello, " + name.capitalize())
#     print("Your age is: " + age)
#     print("function hello is being called")
#
#
# hello()


# Example 2
def hello(name, age):
    print("Hello, " + name.capitalize())
    print("Your age is: " + str(age))
    print("function hello is being called")


name_input = "Duy"
age_input = 28

hello(name_input, age_input)
