# reduce() = apply a function to an iterable and reduce it to a single cumulative value
#            performs the function on the first two elements and repeats the process until 1 value remains
#
# reduce(function, iterable)
from functools import reduce
import functools

# combine all letters in the list
letters = ["H", "E", "L", "L", "O"]
# solution 1: brocode
word = functools.reduce(lambda x, y: x + y, letters)
print(word)



# solution 2: solve it myself

# scramble = lambda a, b: a + b
# scrambled_word = str(reduce(scramble, letters))
# print(scrambled_word)


# find factorial of a number
factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y: x * y, factorial)
print(result)




