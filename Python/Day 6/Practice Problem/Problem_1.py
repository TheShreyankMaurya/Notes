# WAF to print the length of a list. ( list is the parameter)


def calcLen(list):
    return len(list)


print(calcLen([1, 2, 3, 4, 4, 5, 6, 7]))

# WAF to print the elements of a list in a single line. ( list is the parameter)


def printList(list):
    str = ""
    for el in list:
        str = str + f"{el} "
    return str


print(printList([1, 2, 3, 4, 5]))

# WAF to find the factorial of n. (n is the parameter)


def fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


print(fact(10))

# WAF to convert USD to INR.


def conv(usd):
    return usd * 104


print(conv(90))
