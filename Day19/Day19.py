puzzle_input = 3005290
def white_elephant(elves, wrap=False):
    if not wrap:
        if len(elves) % 2 == 1: wrap = True
        elves = elves[::2]
    else:
        if len(elves) % 2 == 1: wrap = False
        elves = elves[1::2]
    if len(elves)==1: return elves[0]
    return white_elephant(elves, wrap)

#This works but takes too long for large numbers like the puzzle input
def pt2(elves):
    elves = elves[:len(elves)//2] + elves[len(elves)//2 +1:]
    #print('removed', len(elves)//2)
    #elves.pop(len(elves)//2)
    elves = elves[1:] + [elves[0]]
    #print(elves)
    if len(elves) == 1: return elves[0]
    return pt2(elves)
# looking for any patterns
for i in range(2,500):
    elves = [x for x in range(1,i+1)]
    print(pt2(elves), 'i=',i)
'''
if the total num of elves can be represented as 3^x where x is an integer, the 3^x numbered elf will win

Then, incrementing the total num of elves by 1 will restart the winners at elf 1
As the total num continues to increment by 1, the winning elf num will also increment by 1
This pattern is followed until the winning elf number is 3^x (the previous highest number elf winner)

After that, an increment of 1 to the total elves increments the winning elf by 2 until the next 3^x is reached

For example, if total num of elves is 27, that means elf 27 will win because 3^3=27
Then, the pattern in format (total, winner) will be (28,1) (29,2), (30, 3) and so on until (54, 27)
Now that the previous 3^x (x=3 in this case) has been reached as a winner again, the pattern increments the winner by 2:
(55, 29), (56, 31), (57, 33) and so on until (81, 81) 
81 can be represented as 3^x where x=4 and the cycle starts over
'''

import math
def run(elf_ct):
    x = math.floor(math.log10(elf_ct)/math.log10(3)) #rounds to lowest int of x so that 3^x is <= elf_ct
    calculated = pow(3,x) #calculates 3^x so that we know what num to count to
    #print('calculated', calculated)
    if calculated == elf_ct: #if elf_ct is 3^x that elf wins
        #print('winner', elf_ct)
        return elf_ct
    winner = elf_ct - calculated 
    if winner > calculated:
        winner = calculated + (winner-calculated)*2
    return winner


#using log10 instead of base 3 to get integer outputs, like log_3(243)=4.9999... but using log10 gets 5
# for i in range(27, 83):
    # print('winner',pattern(i), 'total:', i)

# print(run(puzzle_input))





