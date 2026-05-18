# recursion - when a function calls itself repeatedly.
# base case - it is the condition when we have to stop the recursion.


def show(n):
    if n == 0:  # base case
        return
    print(n)
    show(n - 1)


show(5)


def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))
