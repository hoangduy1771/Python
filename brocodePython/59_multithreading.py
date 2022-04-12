# thread = a flow of execution. like a seperate order of instructions.
# only each thread takes a turn running to achieve the concurrency (sequentially is the opposite)

# io bound = program/task spends most of it's time waiting for external events (user input, webscraping)
#  => use multithreading

import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(5)
    print("You finish studying")


begin_time = time.perf_counter()

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

# eat_breakfast()
# drink_coffee()
# study()

# find a thread that is running
print(threading.active_count())

# print a list of all the thread that is running
print(threading.enumerate())

# measure performance of the main thread
print(time.perf_counter() - begin_time)
