import os

file1 = open("input.txt", "r")
Lines = file1.readlines()

score = 0

for line in Lines:
    if "X" in line: # lose
        if "A" in line:  # they pick rock i pick scissors 
            score = score + 3
        elif "B" in line: # they pick paper i pick rock
            score = score + 1
        else: # they pick  scissors i pick paper
            score = score + 2
    elif "Y" in line: # draw 
        if "B" in line: # paper paper
            score = score + 2 + 3
        elif "A" in line: # rock rock
            score = score + 1 + 3
        else: # scissors scissors
            score = score + 3 + 3
    elif "Z" in line:
        if "C" in line:
            score = score + 1 + 6
        elif "B" in line:
            score = score + 3 + 6
        else:
            score = score + 2 + 6
print(score)
