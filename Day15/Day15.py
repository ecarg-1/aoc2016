with open('input.txt','r') as f: disc_list = [[lines.strip('\n').split(' ')[1],int(lines.strip('\n').split(' ')[3]),int(lines.strip('\n').split(' ')[-1][:-1])] for lines in f.readlines()]
f.close()
def get_capsule(time): #if button is pressed at given time, returns true a capsule will come out or false it won't
    disc_count = 1 #tracks discs since it takes 1 sec to reach a new disc
    for disc in disc_list: #disc in format [disc name, # positions, starting position]
        if (disc[-1]+time+disc_count)%disc[1] !=0: return False #position based on starting position, button time, and how many other discs there were above modulus 0 to get position
        disc_count+=1 #increments disc count
    return True
def run(): #starts at time 0 and runs until it find a time that releases a capsule
    sec = 0
    while(True):
        if get_capsule(sec): break
        sec += 1
    return sec
print(run())
disc_list.append(['newdisc',11,0]) #appending another disc with 11 positions starting at 0
print(run())