# Write a recursive function to calculate the sum of first n natural numbers.


def sum(n):
    if n == 0:
        return 0

    return n + sum(n - 1)


print(sum(5))

# Write a recursive function to print all elements in a list.


def printEl(list, idx):
    if idx == (len(list)):
        return
    print(list[idx])
    printEl(list, idx + 1)


printEl([1, 2, 3, 4, 5], 0)
