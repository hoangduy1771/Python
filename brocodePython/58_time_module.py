from cgi import print_arguments
import time

# find the epoch (when a computer thinks time began)
# c.time method will convert a time expressed in seconds since epoch to a readable string
print(time.ctime(0))

# return current second since epoch
print(time.time())

# get current date and time
print(time.ctime(time.time()))

time_object = time.localtime()
print(time.strftime("%I:%M:%S %p %A, %d %B %Y ", time_object))

# take in a tuple of time and print it out
# (year, month, day, hours, minutes, seconds, day of the week, day of the year, daylight saving time)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
print(time.asctime(time_tuple))

# takein a tuple of time and print it out as seconds
# (year, month, day, hours, minutes, seconds, day of the week, day of the year, daylight saving time)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
print(time.mktime(time_tuple))
