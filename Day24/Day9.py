def day9_2015(perm:list, distances:dict):
    min_dist = 0
    for route in perm:
        cur_dist = 0
        for i in range(len(route)-1):
            try: #since they keys are tuples tries (a,b)
                cur_dist += distances[(route[i], route[i+1])] #adds distance to total current distance
            except KeyError: #if that doesn't work then tries (b,a) to get distance
                cur_dist += distances[(route[i+1],route[i])]
        if min_dist==0 or cur_dist < min_dist: min_dist = cur_dist
    return min_dist
