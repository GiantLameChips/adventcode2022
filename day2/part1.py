import os

file1 = open("input.txt", "r")
Lines = file1.readlines()

score = 0

for line in Lines:
    if "X" in line:
        score = score + 1
        if "A" in line:
            score = score + 3
        elif "C" in line:
            score = score + 6
    elif "Y" in line:
        score = score + 2
        if "B" in line:
            score = score + 3
        elif "A" in line:
            score = score + 6
    elif "Z" in line:
        score = score + 3
        if "C" in line:
            score = score + 3
        elif "B" in line:
            score = score + 6
print(score)
