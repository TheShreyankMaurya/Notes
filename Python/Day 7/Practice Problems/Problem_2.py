# WAF that replace all occurrences of “java” with “python” in above file.

with open("Python/Day 7/Practice Problems/practice.txt", "r") as f:
    data = f.read()

newData = data.replace("Java", "Python")

with open("Python/Day 7/Practice Problems/practice.txt", "w") as f:
    f.write(newData)
