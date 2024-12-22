with open('input.txt','r') as f:
    initial = [[int(line.strip('\n').split(' ')[1]), int(line.strip('\n').split(' ')[-1])] for line in f.readlines() if line[:5] == 'value'] #value,bot
    f.seek(0,0)
    instructions = [line.strip('\n').split(' ') for line in f.readlines() if line[:5] != 'value']
    f.close()
bot_dict, output_dict = dict(), dict()
for i in initial: #assigns initial chips to bots
    if i[-1] in bot_dict.keys(): bot_dict[i[-1]].append(i[0])
    else: bot_dict[i[-1]] = [i[0]]
l, h = 17, 61
while(len(instructions)!=0):
    for ins in instructions:
        giver_bot = int(ins[1])
        if giver_bot in bot_dict.keys() and len(bot_dict[giver_bot]) == 2: #bot is in dict and has 2 chips ready
            lc, hc, lbo, hbo, bol, boh = min(bot_dict[giver_bot]), max(bot_dict[giver_bot]), int(ins[6]), int(ins[-1]), ins[5], ins[-2]
            if lc == l and hc == h: print('Bot', giver_bot)
            if bol == 'bot':
                if lbo in bot_dict.keys(): bot_dict[lbo].append(lc)
                else: bot_dict[lbo] = [lc]
            else: output_dict[lbo] = lc
            if boh == 'bot':
                if hbo in bot_dict.keys(): bot_dict[hbo].append(hc)
                else: bot_dict[hbo] = [hc]
            else: output_dict[hbo] = hc
            instructions.remove(ins)
        else: continue
print(output_dict[0]*output_dict[1]*output_dict[2])