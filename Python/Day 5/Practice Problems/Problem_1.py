# Print numbers from 1 to 100

i = 1
while i <= 100:
    print(i)
    i += 1


# # Print numbers from 100 to 1

j = 100

while j >= 1:
    print(j)
    j -= 1


# Print multiplication table of number n

n = int(input("Enter a number : "))
k = 1
while k <= 10:
    print(f"{n}x{k}=", n * k)
    k += 1

# Print the elements of the following list using loop

a = 0
b = 1
list = []
while a < 100:
    # print(a + b)
    list.append(a + b)
    a += b
    b += 2

# Search for a number x in the list using loop

c = 0
while c < len(list):
    if list[c] == 36:
        print("element found at ", c)
        break
    else:
        print("Finding...")
        c += 1
        continue
