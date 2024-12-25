from hashlib import md5
salt = 'ihaygndm'

def repeats(string, quantity, letter=False):
    for i in range(len(string)-quantity+1):
        if letter:
            if string[i] == letter and string[i:i+5].count(letter) == 5: return True, ''
        elif string[i:i+3].count(string[i]) == 3: return True, string[i]
    return False, ''
def hash_loop(loop, saltstr):
    hexa = md5(saltstr.encode()).hexdigest()
    for _ in range(loop): hexa = md5(hexa.encode()).hexdigest()
    return hexa
def my_func(salt, loop):
    index, keyes = 0, 0
    start_int, end_int, cur_start_ind, cur_end_ind, hashed = 0, 0, 0, 0, [] #new start and end indexes used to create the new hashes, the current start and end index that the hash is based on
    while keyes != 64:
        hexa = hash_loop(loop, salt+str(index))
        r3, let = repeats(hexa,3)
        if r3:
            start_int, end_int = index + 1, index + 1000 #sets the new start and end index to the key index + 1 and a thousand after that
            if len(hashed) == 0: hashed = [hash_loop(loop, salt + str(i)) for i in range(start_int,end_int+1)] #adds the hashes to a list based on the start and end index for first 3 pattern hash
            elif start_int <= cur_end_ind: #if the index of the needed hashes overlaps what is already there
                hashed = hashed[start_int-cur_start_ind:] #the already made 1000 hashes is reduced by cutting off the beginning up to the new start index which is now hashed[0]
                needed = 1000-len(hashed) #how many more hashes are needed to complete the 1000 hash array
                for _ in range(1, needed+1): hashed.append(hash_loop(loop, salt + str(cur_end_ind + _))) #appends the hash based on the current end ind + the loop num 
            for new_hexa in hashed: 
                if repeats(new_hexa, 5, let)[0]:
                    keyes+=1
                    break
            cur_end_ind, cur_start_ind = end_int, start_int
        if keyes != 64: index +=1
    print(index)
my_func(salt, 0) #part 1
my_func(salt, 2016) #part 2
