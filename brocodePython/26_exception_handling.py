# exception = event detected during execution that interupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("Can't be divided by zero")
except ValueError:
    print("Please input number only")
except Exception:
    print("Something went wrong")
else:
    print(result)