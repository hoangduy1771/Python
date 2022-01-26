# tuple = collection which is ordered and unchangeable - similar to list, but immutable
# used to group together related data

student = ("Duy", 25, "male")

print(student.count("Duy"))
print(student.index(25))

print(student)

for i in student:
    print(i)

if "male" in student:
    print("the value is in student tuple")
else:
    print("the value is not in the tuple")
