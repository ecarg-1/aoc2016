with open('input.txt','r') as f:
    ins = [line.strip('\n').split(' ') for line in f.readlines()]
    f.close()
reg, i = {'a': 0, 'b':0, 'c':1, 'd':0}, 0 #c=0 for part1 and c=1 for part 2
while(i<len(ins)):
    a,b,c,d = reg['a'],reg['b'],reg['c'],reg['d'] #so I can use eval 
    match ins[i][0]:
        case 'cpy': reg[ins[i][-1]] = reg[ins[i][1]] if ins[i][1] in reg.keys() else int(ins[i][1])
        case 'jnz': i = i + int(ins[i][-1]) - 1 if ins[i][1] in reg.keys() and reg[ins[i][1]] != 0 or eval(ins[i][1]) != 0 else i
        case 'dec': reg[ins[i][-1]] -= 1
        case 'inc': reg[ins[i][-1]] += 1
    i+=1
print(reg)