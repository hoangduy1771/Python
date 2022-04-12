# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc...)
#                   create a zip object with paired elements stored in tuples for each element
#                   zip object group paired elements into tuples

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")

# zip type
users = zip(usernames, passwords)

for i in users:
    print(i)
print(type(users))
print("========================================")

# convert to list
users = list(zip(usernames, passwords))
print(users)
print(type(users))
print("========================================")

# convert to dictionary
users = dict(zip(usernames, passwords))
for key, value in users.items():
    print(key, value)
print(users)











