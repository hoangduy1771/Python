# filter() = create a collection of elements from an iterable for which a function returns true

#  filter(function, iterable)

friends = [("Rachel", 19),
           ("Monica", 18),
           ("Phoebe", 17),
           ("Joey", 16),
           ("Chandler", 21),
           ("Ross", 20)]

drink_age_filter = lambda age: age[1] >= 18

# def drink_age_filter(age):
#     if age[1] >= 18:
#         return True
#     else:
#         return False

drinking_buddies = list(filter(drink_age_filter, friends))
print(drinking_buddies)












