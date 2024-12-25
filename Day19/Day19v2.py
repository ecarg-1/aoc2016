puzzle_input = 3005290
def white_elephant(elves, wrap=False):
    if not wrap: #wrap means start removing even indexes, no wrap means start removing odd
        if len(elves) % 2 == 1: wrap = True #if it starts not wrapped but has an odd length, it will wrap
        elves = elves[::2]
    else:
        if len(elves) % 2 == 1: wrap = False #if it is wrapped but has an odd number, it will not be wrapped 
        elves = elves[1::2]
    if len(elves)==1: return elves[0] #once there is only 1 elf left, returns the winner
    return white_elephant(elves, wrap)

import math
def run(elf_ct):
    x = math.floor(math.log10(elf_ct)/math.log10(3)) #rounds to lowest int of x so that 3^x is <= elf_ct
    calculated = pow(3,x) #calculates 3^x so that we know what num to count to
    if calculated == elf_ct: return elf_ct#if elf_ct is 3^x that elf wins
    winner = elf_ct - calculated 
    if winner > calculated: winner = calculated + (winner-calculated)*2
    return winner
elves = [x for x in range(1,puzzle_input+1)]
print(white_elephant(elves)) #part1
print(run(puzzle_input))#part2

