# Print the elements of the following list using for loop

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in list:
    print(el)

# Search for a number x in this tuple using for loop

x = int(input("Enter the number to be searched : "))
i = 0
for el in list:
    if el == x:
        print("Element found at", i)
        break
    else:
        i += 1
        continue
