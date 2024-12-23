input = 1358
goal = (31,39)

def state(c,r):
    return str(bin(c*c+3*c+2*c*r+r+r*r+input)).count('1')%2==0

def advance(indices):
    ret_urn = []
    for index in indices:
        x, y = (i for i in index)
        if x!=0 and (x-1,y) not in visited and state(x-1,y): #move left
            visited.add((x-1,y))
            ret_urn.append((x-1,y))
        if y!=0 and (x,y-1) not in visited and state(x,y-1): #move up
            visited.add((x,y-1))
            ret_urn.append((x,y-1))
        if (x+1,y) not in visited and state(x+1,y): #move right
            visited.add((x+1,y))
            ret_urn.append((x+1,y))
        if (x,y+1) not in visited and state(x,y+1): #move down
            visited.add((x,y+1))
            ret_urn.append((x,y+1))
    return ret_urn

visited, here, steps = set(), [(1,1)], 0
while goal not in visited:
    here = advance(here)
    steps += 1
    if steps == 50:
        print(len(visited))
print(steps)