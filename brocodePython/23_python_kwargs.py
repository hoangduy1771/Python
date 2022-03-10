# kwargs = same with args, but have a few differences:
#   1. kwargs pack all arguments into a dictionary.
#   2. kwargs only takes in keywords arguments while args takes in positional arguments


def hello(**kwargs):
    print("Hello, " + kwargs["first"])
    for key,value in kwargs.items():
        print(value)
        print(key)


hello(first="Pham", last="Duy", middle="Hoang")
