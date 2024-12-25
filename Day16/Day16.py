puzzle_input = '01111001100111011'
disk_length = 272
complement = {'1':'0', '0':'1'} #used to complement 
def fill_disk(string, length): #fills a disk of size length starting with string
    while len(string) < length: #while the is smaller than the disk size
        a, b = string, '' #a is same as string and b is empty
        for x in string[::-1]: b = b + complement[x] #b becomes the complement of the reverse string
        string = a + '0' + b #new string 
    return string[:length] #once it is >= disk size, returns only the disk size string
def checksum(string): 
    cs = '' #starts with empty checksum
    while len(cs)%2 != 1: #runs until an odd length checksum found
        cs = '' #every loop resets checksum
        for i in range(0, len(string)-1,2): #goes by 2s
            if string[i]==string[i+1]: cs += '1' #matched
            else: cs += '0' #unmatched
        string = cs #sets string to checksum for next loop
    return cs

a = fill_disk(puzzle_input, disk_length)
print(checksum(a))
b = fill_disk(puzzle_input, 35651584)
print(checksum(b))

