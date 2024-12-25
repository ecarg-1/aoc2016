from itertools import permutations
with open('input.txt','r') as f:
    scrambles = [line.strip('\n').split(' ') for line in f.readlines()]
    f.close()
def scramb(string):
    for x in scrambles:
        match ' '.join(x[:2]):
            case 'swap position': 
                a, b, new_str= int(x[2]), int(x[-1]), ''
                for i in range(len(string)):
                    if i == a: new_str += string[b]
                    elif i == b: new_str += string[a]
                    else: new_str += string[i]
                string = new_str
            case 'swap letter': 
                swap, new_str = {x[2]:x[-1], x[-1]:x[2]}, ''
                for chr in string:
                    if chr in swap.keys(): new_str += swap[chr]
                    else: new_str += chr
                string = new_str
            case 'rotate left': 
                steps = int(x[2])
                string = string[steps:] + string[:steps]
            case 'rotate right':
                steps = int(x[2]) 
                string = string[-steps:] + string[:-steps]
            case 'rotate based': 
                str_list = [chr for chr in string]
                ind = str_list.index(x[-1]) 
                if ind >= 4: ind = (ind + 2) % len(string)
                else: ind = (ind + 1) % len(string)
                string = string[-ind:] + string[:-ind]
            case 'reverse positions': 
                section = string[int(x[2]):int(x[-1])+1]
                string = string[:int(x[2])] + section[::-1] + string[int(x[-1])+1:] 
            case 'move position': 
                str_list = [chr for chr in string]
                popped_chr = str_list.pop(int(x[2]))
                str_list.insert(int(x[-1]),popped_chr)
                string = ''.join(str_list)
    return string
def rev_scramb(goal): #seemed easier/faster than writing a bunch of reverse scramble functions to just brute force through every possible input
    letters = [chr for chr in goal]
    perms = list(permutations(letters))
    for p in perms:
        s = ''.join(p)
        if scramb(s) == goal:
            return s
puzzle_input = 'abcdefgh'   
goal = 'fbgdceah'
print(scramb(puzzle_input)) #part 1
print(rev_scramb(goal))

