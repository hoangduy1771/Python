import random

x = random.randint(0, 10)
print(x)

# random floating point number
y = random.random()
print(y)

myList = ["rock", "paper", "scissor"]
z = random.choice(myList)
print(z)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

random.shuffle(cards)
print(cards)

