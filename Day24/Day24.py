from itertools import permutations
from Day9 import day9_2015
f = open('input.txt', 'r') 
grid = [line.strip('\n') for line in f.readlines()]
f.close()

location_dict = {grid[r][c] : (r,c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c].isnumeric()}   #dict with keys as the numbers and values as their location
max_num = len(location_dict)
'''
At first I had curps and new_curps as lists and it was insanely slow. I changed them to sets and it was way faster
'''
def find_distances(num:str, other_nums:list[str]):
    curps = set([location_dict[num]])
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    visited, cur_dist, return_dict = [], 0, {}
    while len(return_dict) != len(other_nums):
        new_curps = set()
        cur_dist += 1
        for curp in curps:
            for d in directions:
                p, symbol = (curp[0]+d[0], curp[1]+d[1]), grid[curp[0]+d[0]][curp[1]+d[1]]  #position
                if symbol != '#' and p not in visited: 
                    new_curps.add((p))
                    if symbol in other_nums: return_dict[(num, symbol)] = cur_dist
        visited += curps
        curps = new_curps
    return return_dict
numbers, all_dist_dict = [str(i) for i in range(max_num)], {}
for i in range(max_num): all_dist_dict.update(find_distances(str(i), numbers[i+1:]))

numbers.remove('0')
perms_pt1 = [['0'] + list(p) for p in permutations(numbers)]
print(day9_2015(perms_pt1, all_dist_dict)) #pt 1
perms_pt2 = [p + ['0'] for p in perms_pt1]
print(day9_2015(perms_pt2, all_dist_dict)) #pt 2

