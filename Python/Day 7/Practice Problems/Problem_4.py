# WAF to find in which line of the file does the word “learning” occur first. Print -1 if word not found.


def findLine():
    data = True
    count = 1
    with open("Python/Day 7/Practice Problems/practice.txt", "r") as f:
        while data:
            data = f.readline()
            if "lxearning" in data:
                print(f"Found at {count}")
                return
            count += 1
    return -1


findLine()
