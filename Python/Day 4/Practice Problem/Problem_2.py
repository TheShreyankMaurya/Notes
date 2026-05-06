# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

dict = {}

sub1 = input("Enter name of subject 1 : ")
mark1 = int(input(f"Enter marks of {sub1} : "))

dict.update({sub1: mark1})

sub2 = input("Enter name of subject 2 : ")
mark2 = int(input(f"Enter marks of {sub2} : "))

dict.update({sub2: mark2})

sub3 = input("Enter name of subject 3 : ")
mark3 = int(input(f"Enter marks of {sub3} : "))

dict.update({sub3: mark3})

print(dict)
