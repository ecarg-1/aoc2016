f = open('input.txt','r')
ins = [line.strip('\n').split() for line in f.readlines()]
f.close()
rega = 0            #starts register a at 0     
while True:
    reg = {chr(i):0 for i in range(97,101)} #resets register 
    reg['a'] = rega                         #sets a to rega (increments with each loop)
    i,output,check,states,done= 0,'',False,[],False #index of instruction, output transmission (ex '01010101'), check bool to check for errors in transmission, register states + index, found answer bool
    while i < len(ins):
        a = ins[i][1] if ins[i][1].isalpha() else int(ins[i][1])
        if len(ins[i]) == 3: b = ins[i][2] if ins[i][2].isalpha() else int(ins[i][2])
        match ins[i][0]:
            case 'cpy': reg[b] = a if isinstance(a, int) else reg[a]
            case 'inc': reg[a] += 1
            case 'dec': reg[a] -= 1
            case 'jnz':
                jump = b if isinstance(b, int) else reg[b]
                zero = a if isinstance(a, int) else reg[a]
                if zero != 0: i += jump - 1
            case 'out': 
                output += str(reg[a])          #always contains just 1s or 0s, adds to output
                check = True                   #triggers the output to be checked 
        if check:                              #checking sequence
            if output.count('11') > 0 or output.count('00') > 0 or output[0] == '1': break      #must start with 0, must alternate, breaks to next rega value if not
            cur_state = [val for val in reg.values()] + [i]                                     #state = [a,b,c,d,i] (values of registers)
            if cur_state in states:                                                             #if this state has been seen before
                done = True                                                                     #t's done and will repeat again forever
                break                                                                           #breaks the inner while loop
            else: states.append(cur_state)                                                      #appends unseen state
        i += 1                                                                                  #inc instruction
    if done: break                                                                              #breaks outter while loop once answer is found
    rega += 1
print(rega)     #prints answer, kinds slow though