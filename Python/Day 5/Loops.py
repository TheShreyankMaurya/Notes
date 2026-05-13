# Loops - are used to repeat instructions.

# while Loop

i = 1
while i <= 5:
    print("Hello World!")
    i += 1


# Break - used to terminate the loop when encountered.

# Continue - terminates execution in the current iteration and continue the execution of the loop with the next iteration.

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

c = 0
while c < len(list):
    if list[c] == 36:
        print("element found at ", c)
        break
    else:
        c += 1
        continue


# for Loop - generally used for sequential traversal.

for el in list:
    print(el)

for el in list:
    print(el)
else:
    print("List end's here")


# range - it returns a sequence of numbers, starting from 0 by default and increments by 1(by default) and stops before a specified number.
# syntax - range(start,stop,step)

for el in range(5):
    print(el)

for el in range(1, 5):
    print(el)

for el in range(1, 10, 2):
    print(el)

# pass - it is a null statement that does nothing. It is used as a placeholder for future code.

for el in range(1):
    pass
