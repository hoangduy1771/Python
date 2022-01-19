# slicing = create a substring by extracting elements from another string
# using indexing operator [] or slice()
#  [start:stop:step]

# indexing
name = "Pham Hoang Duy"
first_name = name[:4]
last_name = name[5:]
funky_name = name[::2]
print(first_name)
print(last_name)
print(funky_name)

reversed_name = name[::-1]
print(reversed_name)

# slice
website1 = "http://google.com"
website2 = "http://brocode.com"

sliced = slice(7, -4)

print(website1[sliced])
print(website2[sliced])


