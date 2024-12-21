import re
with open('input.txt','r') as f:
    ips = [re.split(r'\[|\]', line.strip('\n')) for line in f.readlines()] 
    f.close()
def find_pattern_abba(string):
    for i in range(len(string)-3):
        if string[i] != string[i+1] and string[i+1] == string[i+2] and string[i+3]==string[i]: return True
    return False
def find_pattern_aba(string):
    aba = []
    for i in range(len(string)-2):
        if string[i]!=string[i+1] and string[i]==string[i+2]:
            aba.append(string[i:i+3])
    if len(aba) > 0: return True, aba
    return False, []
total1, total2 = 0, 0
for ip in ips:
    abba, hypernet, aba, bab = False, False, [], []
    for i in range(len(ip)):
        if i%2 == 0: 
            if find_pattern_abba(ip[i]): abba = True
            if find_pattern_aba(ip[i])[0]: aba += find_pattern_aba(ip[i])[1]
        else: 
            if find_pattern_abba(ip[i]): hypernet = True
            if find_pattern_aba(ip[i])[0]: bab += find_pattern_aba(ip[i])[1]
    if abba and not hypernet: total1+=1
    for i in range(len(aba)): aba[i] = aba[i][1]+aba[i][0]+aba[i][1]
    if len(set(aba) & set(bab)) > 0: total2+=1
print(total1, total2)
