# WAP to check if a list contains a palindrome of elements.

list = [1, "abc", "abc", 1]

listCopy = list.copy()
listCopy.reverse()

if list == listCopy:
    print("List is palindrome")
else:
    print("List is not palindrome")
