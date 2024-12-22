input = 1358
#input =397
goal = [7,9]
#goal = [31, 39] #c,r
start = [1,1]
paths = []

# def state(r,c): #given an index, the state of that index is returned (space or wall)
#     ones = str(bin(c*c + 3*c + 2*c*r + r + r*r + input))[2:].count('1')
#     if ones%2==0: return '.' #space
#     else: return '#' #wall
def state(r,c): #given an index, the state of that index is returned (space or wall)
    ones = str(bin(c*c + 3*c + 2*c*r + r + r*r + input))[2:].count('1')
    return ones%2==0 #space

def find_path(c, r, g, visited, count): #row, col, goal
    if c == g[0] and r == g[1]: return count
    if c < 0 or r < 0: return 'nothing'
    options = {'right':state(r,c+1), 'left':state(r,c-1), 'down':state(r+1,c), 'up':state(r-1,c)} #right, left, down, up
    visited += [[c,r]]
    valid_moves = [move for move in options.keys() if options[move]]
    #print()
    #print(valid_moves, c, r)
    for move in valid_moves:
        #print('move:',move, 'from', c,r)
        #print('visited ind:', visited)
        a, nr, nc = 'nothing', r, c
        match move:
            case 'right': nc = c+1
            case 'left': nc = c-1
            case 'down': nr = r+1
            case 'up': nr = r-1
        if [nc, nr] in visited: continue
        else: a = find_path(nc,nr,g,visited,count+1)
    #if no move is able to be made, a dead end has been reached
        if isinstance(a, int): 
            print('appending', c, r, move)
            #print(visited)
            paths.append(a)
    #print('no valid move')
    return a

'''
Given the current index, find the states of the four possible directions
The priority of moves should be:
    Toward row goal
    Toward col goal
    Away from row
    Away from col
    if position repeated, invalid sequence
'''

(find_path(start[0],start[1],goal,[],0))
print(paths)
