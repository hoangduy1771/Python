# Loop Control Statements = change a loops execution from its normal sequence

# break = terminate loop
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

# break example
while True:
    name = input("Enter your name: ")
    if name != "":
        break

# continue example
phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

# pass example
for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)
