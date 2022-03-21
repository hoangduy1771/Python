# map() = applied to a function to each item in an iterable (list, tuple, etc..)
# map(function, iterable)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

to_vnd = lambda data: (data[0], data[1] * 23000)
to_usd = lambda data: (data[0], data[1] / 23000)
store_vnd = list(map(to_vnd, store))
store_usd = list(map(to_usd, store_vnd))

for i in store_vnd:
    print(i)

print("=======================")

for i in store_usd:
    print(i)
