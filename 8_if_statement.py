age = None

while age is None:
    input_value = input("How old are you?: ")
    print("You typed: " + input_value)
    try:
        age = int(input_value)
    except ValueError:
        print("Invalid input. Please type your age again, numbers only")

if int(age) < 1:
    print("Invalid age")
elif int(age) > 18:
    print("You're old enough to purchase alcohol")
elif int(age) < 18:
    print("You're not old enough to purchase alcohol")
else:
    print("You can purchase alcohol, but your choice is limited")
