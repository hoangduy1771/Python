# keyword argument = arguments preceded with an identifier when we pass them to a 18_functions
#                     order of the arguments doesn't matter, unlike positional arguments
#                     Benefit of keyword arguments: Python knows the name of the arguments that our function receives

def hello(first, middle, last):
    print("Hello, " + first + " " + middle + " " + last)


hello(last="Duy", first="Pham", middle="Hoang")
