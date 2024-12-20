with open('input1.txt','r') as f:
    directions = f.read().split(', ')
    f.close()
cur_dir, visited_locations, dir_dict, pt2 = 0, [], {0: 0, 1: 0, 2:0, 3:0}, False
for d in directions:
    if d[0] == 'R': cur_dir = (cur_dir + 1) % 4
    else: cur_dir = (cur_dir - 1) % 4
    for i in range(int(d[1:])):
        dir_dict[cur_dir] += 1
        cur_pos = [dir_dict[0]-dir_dict[2], dir_dict[1]-dir_dict[3]]
        if cur_pos in visited_locations and not pt2: 
            print('part 2: ', abs(cur_pos[0]) + abs(cur_pos[1]))
            pt2 = True
        else: visited_locations.append(cur_pos)
print('part 1: ', abs(cur_pos[0]) +abs(cur_pos[1]))