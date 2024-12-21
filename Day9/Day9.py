with open ('input.txt','r') as f:
    data = f.read()
    f.close()
def decompress(data, part):
    i, total = 0, 0
    while(i<len(data)):
        if data[i] == '(':
            i, cur_str = i+1, ''
            while(data[i]!=')'):
                cur_str+=data[i]
                i+=1
            if part == 1: total += int(cur_str.split('x')[0])*int(cur_str.split('x')[1])
            else: total += int(cur_str.split('x')[1])*decompress(data[i+1:i+1+int(cur_str.split('x')[0])], 2)
            i+=int(cur_str.split('x')[0])
        else: total+=1
        i+=1
    return total
print(decompress(data, 1), decompress(data, 2))