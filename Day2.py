with open('input2.txt','r') as f:
    direction = [line.strip('\n') for line in f.readlines()]
    f.close()
#Part 1
nums = {(-1,1):'1', (0,1):'2', (1,1):'3', (-1,0):'4', (0,0):'5', (1,0):'6', (-1,-1):'7', (0,-1):'8', (1,-1):'9'}
cur_pos, code = [0,0], ''
for line in direction:
    for l in line:
        match l:
            case 'U': cur_pos[1] = cur_pos[1] + 1 if cur_pos[1] + 1 < 2 else 1 
            case 'D': cur_pos[1] = cur_pos[1] - 1 if cur_pos[1] - 1 > -2 else -1 
            case 'L': cur_pos[0] = cur_pos[0] - 1 if cur_pos[0] - 1 > -2 else -1 
            case 'R': cur_pos[0] = cur_pos[0] + 1 if cur_pos[0] + 1 > 2 else 1 
    code += nums[tuple(cur_pos)]
print(code)

#Part 2
pt2_cur_pos, pt2_pass = [0,0], '' #row,col
row_bounds = {2: [2,2], 1: [1,3], 0: [0, 4], -1:[1,3], -2:[2,2]}
col_bounds = {0:[0,0], 1: [-1,1], 2:[-2,2],3:[-1,1], 4:[0,0]}
keypad = {(2,2):'1',(1,1):'2',(1,2):'3',(1,3):'4',(0,0):'5',(0,1):'6',(0,2):'7',(0,3):'8',(0,4):'9',(-1,1):'A',(-1,2):'B',(-1,3):'C',(-2,2):'D' }
for line in direction:
    for l in line:
        match l: #inc/dec cur_pos based on column and row bounds
            case 'U': cur_pos[0] = cur_pos[0] + 1 if cur_pos[0] + 1 <= col_bounds[cur_pos[1]][1] else col_bounds[cur_pos[1]][1]
            case 'D': cur_pos[0] = cur_pos[0] - 1 if cur_pos[0] - 1 >= col_bounds[cur_pos[1]][0] else col_bounds[cur_pos[1]][0]
            case 'R': cur_pos[1] = cur_pos[1] + 1 if cur_pos[1] + 1 <= row_bounds[cur_pos[0]][1] else row_bounds[cur_pos[0]][1]
            case 'L': cur_pos[1] = cur_pos[1] - 1 if cur_pos[1] - 1 >= row_bounds[cur_pos[0]][0] else row_bounds[cur_pos[0]][0]
    pt2_pass += keypad[tuple(cur_pos)]
print(pt2_pass)