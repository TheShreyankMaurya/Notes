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
