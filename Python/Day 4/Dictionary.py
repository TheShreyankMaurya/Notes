# Dictionary are used to store data in key:value pairs. They are unordered, mutable and does not allow duplicate values.

dict = {
    "name": "Shreyank",
    "cgpa": 8.8,
    "marks": [85, 82, 83],
}

print(dict, dict["name"], dict["marks"])

dict["cgpa"] = 8.86

print(dict["cgpa"])

# Nested dictionary(dictionary inside dictionary).

nesDict = {
    "name": "Shreyank",
    "cgpa": 8.8,
    "marks": {
        "OS": 83,
        "CN": 88,
        "DAA": 82,
    },
}

print(nesDict, nesDict["marks"]["OS"])

# Dictionary methods :-

# keys - returns all keys.
print(nesDict.keys())

# values - returns all values.
print(nesDict.values())

# items - returns all key-value pair as a tuple.
print(nesDict.items())

# get - returns the value of the key.
print(nesDict.get("name"))

# update - insert item to the dictionary.
newDict = {
    "sem": "5th",
    "year": "3rd",
}

nesDict.update(newDict)

print(nesDict)
