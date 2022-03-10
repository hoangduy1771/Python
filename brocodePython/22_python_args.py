# args = parameter that will pack all arguments into a tuple
#       useful so that a function can accept a varying amount of arguments

def add(*args):
    sum_num = 0

    #
    args = list(args)
    args[1] = 0
    #

    for i in args:
        sum_num += i
    return sum_num


print(add(1, 2, 3, 4, 5, 6, 7))
