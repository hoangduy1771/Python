# set = collection which is unordered, unindexed. No duplicate values are

utensils = {"fork", "knife", "spoon"}
dishes = {"bowl", "plate", "cup", "knife"}

# print(utensils)
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes)

dinner_table = utensils.union(dishes)

# for x in utensils:
#     print(x)

for x in dinner_table:
    print(x)

# print out the difference
print(utensils.difference(dishes))

# print out what both have in common
print(utensils.intersection(dishes))
