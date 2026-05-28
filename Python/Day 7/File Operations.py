# Reading a file

f = open("Demo.txt", "r")
data = f.read()
print(data)
f.close()

# Writing a file

f = open("Demo.txt", "a")
f.write("\n I will learn about JavaScript tomorrow.")
f.close()

# with Syntax

with open("Sample.txt", "x") as f:
    f.write(
        "This is a new file creating with 'x' mode and generated using 'with' syntax."
    )

# Deleting a file

import os

os.remove("Sample.txt")
