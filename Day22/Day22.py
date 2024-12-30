import re
with open('input.txt','r') as f:
    nodes = [re.findall(r'x\d{1,2}|y\d{1,2}|\d{1,3}T|\d{1,2}%',line.strip('\n')) for line in f.readlines()][2:]
    f.close()
#size[2], used[3], avail[4], percent[5]
total = 0
for a in nodes:
    for b in nodes:
        total = total + 1 if int(a[3][:-1]) != 0 and a != b and int(a[3][:-1]) <= int(b[4][:-1]) else total
print(total)
