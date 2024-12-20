import hashlib
id = 'abbhdwsy'
num_hashes, i = 0, 0
pt1_password, pt2_password = '', [0,0,0,0,0,0,0,0]
inds = []
while(len(inds) < 8):
    id_int = id + str(i)
    hex = str(hashlib.md5(id_int.encode()).hexdigest())
    if hex[0:5] == '00000':
        if num_hashes < 8:
            pt1_password += hex[5]
            num_hashes +=1
        try:
            if int(hex[5]) < 8 and hex[5] not in inds:
                inds.append(hex[5])
                pt2_password[int(hex[5])] = hex[6]
        except:
            pass
    i+=1
print(pt1_password, ''.join(pt2_password))