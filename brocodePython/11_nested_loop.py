rows = int(input("How many rows you want to print?: "))
columns = int(input("How many columns you want to print?: "))
symbol = input("What symbol do you want to use?")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
