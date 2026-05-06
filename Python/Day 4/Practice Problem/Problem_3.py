# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.

list = [
    "python",
    "java",
    "C++",
    "python",
    "javascript",
    "java",
    "python",
    "java",
    "C++",
    "C",
]

set = set(list)

print("The no. of classrooms required are : ", len(set))
