# WAP to find the greatest of 3 numbers entered by the user.

num1 = int(input("Enter num 1 : "))
num2 = int(input("Enter num 2 : "))
num3 = int(input("Enter num 3 : "))

if num1 > num2 and num1 > num3:
    print("Num 1 is greater.")
elif num2 > num1 and num2 > num3:
    print("Num 2 is greater")
else:
    print("Num 3 is greater")
