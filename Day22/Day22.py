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

'''
I didn't find a code for part 2 but I printed it to make it easier.
The coordinate of the original empty space is (4,25) so it would take 4+25=29 moves to get the empty space to the top left corner
Then you shift the entire first row over which is 29 moves.
Then it takes 5 moves to get the empty space back behind the goal space. The goal space needs to move 28 more times so 28*5 moves
That brings the total to 198
'''
node_dict = {(int(node[0][1:]), int(node[1][1:])): node for node in nodes}
for y in range(35):
    for x in range(30):
        if int(node_dict[(x,y)][3][:-1]) > 100: print('#', end=' ')
        elif int(node_dict[(x,y)][3][:-1]) == 0: print('_', end = ' ')
        else: print('.', end=' ')
    print()