# List - it is a data type in python which stores set of values. It can store different types of elements.

marks = [13, 17, 21, 24, 27]

student = ["Shreyank", 85, "Delhi"]

student[2] = "Dholera"

print(student)

# Lists also supports slicing and is same is strings.

# List methods

list = [2, 1, 3]

# append - adds one element at the end.
list.append(4)
print(list)

# sort - sorts in ascending order. sort(reverse=True) - for desecding order.
list.sort()
print(list)

list.sort(reverse=True)
print(list)

# reverse - reverse the list.
list.reverse()
print(list)

# insert - insert element at a particular index.
list.insert(3, 5)
print(list)

# remove - remove the first occurence of element.
list.remove(1)
print(list)

# pop - remove the element from the end or at idx.
list.pop()
print(list)

list.pop(2)
print(list)
