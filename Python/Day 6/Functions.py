# Function - Block of statement that perform a specific task.

# function for sum of two numbers.


def sum(num1, num2):
    s = num1 + num2
    return s


print(sum(5, 6))

# Types of function:-
# 1. Built-in functions - predefined in python(print,len,type).
# 2. User-defined functions - created by user to perform some task.

# Default parameter - assigning a default value to a parameter, which is used when no argument is passed.


def greet(user="Guest"):
    return f"Hello {user}"


print(greet())
print(greet("Shreyank"))
