# sort() method = used with lists
# sorted() function = used with iterables which includes lists
# sorted takes 2 args, 1st: the list/tuple, 2nd: a key to sort by

students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs"]
students.sort(reverse=True)

for i in students:
    print(i)

letters = ("M", "X", "P", "F", "G", "C", "A", "B", "N")
sorted_letters = sorted(letters, reverse=True)

print(sorted_letters)
for i in sorted_letters:
    print(i)

# keyword arguments
# list of tuples
students = [("Squidward", "F", 60),
            ("Sandy", "A", 15),
            ("Patrick", "D", 17),
            ("Spongebob", "B", 16),
            ("Mr.Krabs", "C", 55)]

# sort by name
print("sorted by name")
students.sort()

for i in students:
    print(i)
print("=====================================")

# sort by grades
print("sorted by grades")
grade = lambda grades: grades[1]
students.sort(key=grade)

for i in students:
    print(i)
print("=====================================")

# sort by age
print("sorted by age")
age = lambda ages:ages[2]
students.sort(key=age)

for i in students:
    print(i)
print("======================================")
# tuples of tuples:
students = (("Squidward", "F", 60),
            ("Sandy", "A", 15),
            ("Patrick", "D", 17),
            ("Spongebob", "B", 16),
            ("Mr.Krabs", "C", 55))

sorted_students = sorted(students, key=age, reverse=True)
for i in sorted_students:
    print(i)















