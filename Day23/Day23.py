f = open('input.txt','r') 
ins = [line.strip('\n').split() for line in f.readlines()]
f.close()
i, reg_dict= 0, {chr(x):0 for x in range(97, 101)}
reg_dict['a'] = 7
while i < len(ins):
    match ins[i][0]:
        case 'cpy': reg_dict[ins[i][2]] = reg_dict[ins[i][1]] if ins[i][1].isalpha() else int(ins[i][1])
        case 'dec': reg_dict[ins[i][1]] -= 1
        case 'inc': reg_dict[ins[i][1]] += 1
        case 'jnz':
            num = reg_dict[ins[i][1]] if ins[i][1].isalpha() else int(ins[i][1])
            jmp = reg_dict[ins[i][2]] if ins[i][2].isalpha() else int(ins[i][2])
            if num != 0: i+= jmp - 1
        case 'tgl': 
            amount, kw = reg_dict[ins[i][1]] if ins[i][1].isalpha() else int(ins[i][1]), ['jnz', 'cpy']
            if i+amount < len(ins) and len(ins[i+amount]) == 2: kw = ['inc', 'dec']
            if i+amount < len(ins) and ins[i+amount][0] == kw[0]: ins[i+amount][0] = kw[1]
            elif i+amount < len(ins): ins[i+amount][0] = kw[0]
    i += 1  

print('Pt1:',reg_dict['a'])
#Part 2
import math
print('Pt2:',math.factorial(12) + 78*70)