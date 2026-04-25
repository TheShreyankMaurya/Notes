# String is a data type that stores a sequence of characters.

# Basic Operations

str1 = "hello"
str2 = "world!"

# Concatenation
print(str1 + str2)

# Length of str
print("length of string 1 is ", len(str1), "and length of string 2 is", len(str2))

str = "Standup Comedy"

# Indexing - it startes from 0 and goes till len - 1, and in reverse it startes from -1 and goes till -len.
print(str[0], str[5])

# Slicing - Accessing parts of a str. (syntax - str[startingIdx:endingIdx] | endingIdx is not included.)
print(str[0:4], str[:5], str[6:], str[-1:-7])

# String Functions

stn = "i am a software developer."

# endswith - returns true if str ends with subStr.
print("The sentance ends with er. : ", stn.endswith("er."))

# capitalize - capitalize first letter.
print("Capitalize : ", stn.capitalize())

# replace - replaces all occurence of old with new.
print("Replaced : ", stn.replace("a", "t"))

# find - returns the index of 1st occurence.
print("Find : ", stn.find("s"))

# count - counts the occurence of substr in str.
print("count of 'a' : ", stn.count("a"))
