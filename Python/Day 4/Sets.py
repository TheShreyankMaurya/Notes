# Set is the collection of unordered elements. each element in the set must be unique & immutable.

num = {1, 2, 2, 1, 3, 4, 5, 6}
print(num)

# Null set
nullSet = set()
print(nullSet)

# Set methods

# add - adds an element to the set.
num.add(7)
print(num)

# remove - removes the element from the set.
num.remove(5)
print(num)

# pop - removes a random value.
num.pop()
print(num)

# clear - empty the set.
num.clear()
print(num)

set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6, 7}

print("Union : ", set1.union(set2))
print("Intersection : ", set1.intersection(set2))
