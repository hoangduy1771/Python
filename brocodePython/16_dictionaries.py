# dictionary = a changable, unordered collection of unique key:value pairs
# fast due to using hash, allow us to access a value quickly

capitals = {'Vietnam': 'Hanoi',
            'Japan': 'Tokyo',
            'USA': 'Washington DC'}
capitals.update({'Germany': 'Berlin'})

# print(capitals['Vietnam'])
# print(capitals['Germany'])

# print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key, value)

