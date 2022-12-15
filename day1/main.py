import os

file1 = open("input.txt", "r")
Lines = file1.readlines()


top = 0
list = []
count = 0
for line in Lines:
    if line.strip() == "":
        if count > top:
            top = float(count)
        list.append(count)
        count = 0
    else:
        count = count + float(line)
list.sort(reverse=True)
print(list[0])
print(list[1])
print(list[2])

print(list[0] + list[1] + list[2])
