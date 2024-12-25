with open('input.txt','r') as f:
    ranges = {int(line.strip('\n').split('-')[0]): int(line.strip('\n').split('-')[1]) for line in f.readlines()}
    f.close()
sr = [[key, ranges[key]] for key in sorted(ranges.keys())] #sorted by ascending by start of each range
def run(part1=True): #works for part1 and part2
    max_banned, allowed_ct = -1, 0 
    for r in sr:
        if r[0] > max_banned + 1: #if the start of the range > the max banned (prob the end of the prev range or greater), then there's a gap of allowed ips
            if part1: return max_banned + 1 #if part 1, then we just want to know the first allowed ip
            allowed_ct += r[0] - (max_banned + 1) #if part 2, then we want to count the allowed ips
        max_banned = max(max_banned, r[1]) #sets the max banned to the end of the current range
    return allowed_ct #returns allowed count if part 2 since part 1 would return before this
        
print(run()) #part 1
print(run(False)) #part 2