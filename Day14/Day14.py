from hashlib import md5
salt = 'ihaygndm'

def repeats(string, quantity, letter=False):
    for i in range(len(string)-quantity+1):
        if letter:
            if string[i] == letter and string[i:i+5].count(letter) == 5:
                #print('5',string[i:i+5])
                return True, ''
        elif string[i:i+3].count(string[i]) == 3: 
            #print('3',string[i:i+quantity])
            return True, string[i]
    return False, ''
def hash_loop(loop, saltstr):
    hexa = md5(saltstr.encode()).hexdigest()
    for _ in range(loop):
        hexa = md5(hexa.encode()).hexdigest()
    return hexa
#####this function did not work well for part 2 having to calculate thousands of the same hashes each loop, pt was running for about 20 hours and didn't find 1/3 of the keys
# def my_func(salt, loop):
#     index, keyes = 0, 0
#     while keyes != 64:
#         hexa = hash_loop(loop, salt+str(index))
#         r3, let = repeats(hexa,3)
#         if r3:
#             start, end = index + 1, index + 1001
#             for i in range(index+1,index+1000):
#                 new_hexa = hash_loop(loop, salt+str(i))
#                 if repeats(new_hexa, 5, let)[0]:
#                     keyes += 1
#                     print('key count',keyes,'for ind',index,'and 5 at ind',i)
#                     break
#         if keyes != 64: index +=1
#     print(index)


def my_func(salt, loop):
    index, keyes = 0, 0
    start_int, end_int, cur_start_ind, cur_end_ind, hashed = 0, 0, 0, 0, [] #new start and end indexes used to create the new hashes, the current start and end index that the hash is based on
    while keyes != 64:#######################
        hexa = hash_loop(loop, salt+str(index))
        r3, let = repeats(hexa,3)
        if r3:
            #print('3 pattern found at index', index)
            start_int, end_int = index + 1, index + 1000 #sets tje new start and end index to the key index + 1 and a thousand after that
            if len(hashed) == 0: #this runs if it is the first instance of a 3 in a row pattern (no hashes stored)
                #print('calculating hashes for', start_int, end_int, 'with index', index)
                hashed = [hash_loop(loop, salt + str(i)) for i in range(start_int,end_int+1)] #adds the hashes to a list based on the start and end index
            elif start_int <= cur_end_ind: #if the index of the needed hashes overlaps what is already there
                #print('cur end is:', cur_end_ind, 'and start of new is:',start_int )
                hashed = hashed[start_int-cur_start_ind:] #the already made 1000 hashes is reduced by cutting off the beginning up to the new start index which is now hashed[0]
                #print('hash shortened starting at ind', start_int-cur_start_ind, 'to a len of', len(hashed))
                needed = 1000-len(hashed) #how many more hashes are needed to complete the 1000 hash array
                #print(accounted_for,'accounted for hashes')
                for _ in range(1, needed+1): #loops based on how many hashes are needed
                    #print('appending salt+', cur_end_ind+_)
                    hashed.append(hash_loop(loop, salt + str(cur_end_ind + _))) #appends the hash based on the current end ind + the loop num 
                #print('new hashed starts at', start_int, end_int)
            
            for new_hexa in hashed: 
                if repeats(new_hexa, 5, let)[0]:
                    keyes+=1
                    break
            #### the for loop below can replace the above for loop and provides a print statement indicating progress
            # for i in range(len(hashed)): 
            #     new_hexa = hashed[i]
            #     if repeats(new_hexa, 5, let)[0]:
            #         keyes += 1
            #         print('key count',keyes,'for ind',index,'and 5 at ind', i+start_int)
            #         #print(new_hexa)
            #         break
            cur_end_ind, cur_start_ind = end_int, start_int
        if keyes != 64: index +=1 ###############
    print(index)

my_func(salt, 2016)
