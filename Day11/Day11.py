'''
I am going to represent the generators as negative numbers and chips as positive numbers. The corresponding pair will be equal but opposite. 



    1 3
E   -1 -2 2 -3 -4 4 -5 5

at least one thing and at most two things can be in the elevator
I'd say that going down, only bring one thing and going up always bring two things
'''
x = [[-1,-2,2,-3,-4,4,-5, 5],[1,3],[],[]]
def valid(floors:list) -> bool:
    for floor in floors:
        if not floor: continue
        all_pos = ([a > 0 for a in floor]).count(True) == len(floor)
        all_neg = ([a < 0 for a in floor]).count(True) == len(floor)
        unpaired = [x for x in floor if -x not in floor]
        unpaired_all_neg = ([p < 0 for p in unpaired]).count(True) == len(unpaired)
        if not all_neg and not all_pos and not unpaired_all_neg: return False
    return True

def 
print(valid(x))