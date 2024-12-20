import re
import statistics
with open('input.txt', 'r') as f:
    rooms = [[''.join(re.split(r'-',line.strip('\n'))[0:-1]), int(re.split(r'-|\[', line.strip('\n'))[-2]),re.split(r'\[|\]', line.strip('\n'))[-2]] for line in f.readlines()]
    f.close()
def real_room(string, checksum):
    actual_cs = ''
    alphabetical = ''.join([chr(j) for j in sorted([ord(i) for i in string])])
    for a in range(5):
        actual_cs += statistics.mode(alphabetical)
        alphabetical = re.sub(statistics.mode(alphabetical), '', alphabetical)
    if actual_cs == checksum: return True
    else: return False
def decipher(string, id):
    new_str = ''
    for i in string:
        ascii_num = ord(i)
        for j in range(id):
            ascii_num = ascii_num+1 if ascii_num+1<123 else 97
        new_str+=chr(ascii_num)
    return new_str
total = 0
for r in rooms:
    if real_room(r[0], r[-1]): 
        total += r[-2]
        if 'northpole' in decipher(r[0], r[-2]):
            print(r[-2])
print(total)
