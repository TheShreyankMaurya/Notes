# Create a new file “practice.txt” using python. Add the following data in it:

with open("Python/Day 7/Practice Problems/practice.txt", "x") as f:
    data = "Hi everyone. \nwe are learning File I/O \nusing Java. \nI like programming in Java"
    f.write(data)
