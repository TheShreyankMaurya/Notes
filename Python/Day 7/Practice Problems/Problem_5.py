# From a file containing numbers separated by comma, print the count of even numbers.

with open("Python/Day 7/Practice Problems/numbers.txt", "r") as f:
    data = f.read()

list = data.split(",")

count = 0

for el in list:
    if int(el) % 2 == 0:
        count += 1
    else:
        continue

print(count)
