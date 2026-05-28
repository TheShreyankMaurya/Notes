# Reading a file

f = open("/Users/macbookair/Desktop/Workspace/Notes/Python/Day 7/Demo.txt", "r")
data = f.read()
print(data)
f.close()

# Writing a file

f = open("/Users/macbookair/Desktop/Workspace/Notes/Python/Day 7/Demo.txt", "a")
f.write("\n I will learn about JavaScript tomorrow.")
f.close()

# with Syntax

with open(
    "/Users/macbookair/Desktop/Workspace/Notes/Python/Day 7/Sample.txt", "x"
) as f:
    f.write(
        "This is a new file creating with 'x' mode and generated using 'with' syntax."
    )

# Deleting a file

import os

os.remove("/Users/macbookair/Desktop/Workspace/Notes/Python/Day 7/Sample.txt")
