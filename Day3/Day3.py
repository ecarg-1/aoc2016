import re
with open("input.txt", "r") as file:
    triangles = [re.findall(r"\d{1,3}", line) for line in file.readlines()]
file.close()
#Part 1
count=0
for t in triangles:
    sides = sorted([int(t[i]) for i in range (0,3)])
    if sides[0]+sides[1] > sides[2]:
        count = count+1
print(count)
#Part 2
c = 0
for i in range(0, len(triangles), 3):
    for j in range(0,3):
        side = sorted([int(triangles[i][j]), int(triangles[i+1][j]), int(triangles[i+2][j])])
        if (side[0]+side[1])>side[2]:
            c = c + 1
print(c)