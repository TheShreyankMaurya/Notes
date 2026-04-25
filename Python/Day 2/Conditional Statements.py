# Conditional Statements - are used to make the program to take decision on the basis of some condition.

"""
Syntax :-
if condition:
    Statement1
elif condition :
    Statement2
else:
    StatementN
"""

# Example - Grade of students based on marks

marks = int(input("Enter your marks : "))

if marks >= 90:
    print("Grade : O")
elif marks < 90 and marks >= 75:
    print("Grade : A+")
elif marks < 75 and marks >= 65:
    print("Grade : A")
else:
    print("Grade below B")
