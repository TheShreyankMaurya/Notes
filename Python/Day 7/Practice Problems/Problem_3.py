# Search if the word “learning” exists in the file or not.

with open("Python/Day 7/Practice Problems/practice.txt", "r") as f:
    data = f.read()

i = data.find("learning")

if i > -1:
    print("file contain the word 'learning'.")
else:
    print("file does not contain the word 'learning'.")
