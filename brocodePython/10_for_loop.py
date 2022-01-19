import time

# for i in range(10):
#     print(i)

# for i in range(50, 100 + 1, 2):
#     print(i)

# for i in "giraffe":
#     print(i)

seconds_start = 15
for seconds in range(seconds_start, 0, -1):
    print(seconds)
    time.sleep(1)

print(str(seconds_start) + " has passed")
