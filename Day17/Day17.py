from hashlib import md5
passcode = 'qljzarfv'
start = [1,1]
# b c d e f = open, a 0-9 = close
def find_hash(string):
    return md5(string.encode()).hexdigest()

def valid_moves(options): 
    open_chr, moves = ['b','c','d','e','f'], []
    for x in options:
        path, position = x[0], x[1]
        hashed = find_hash(passcode + path)[:4]
        if hashed[0] in open_chr and position[1] != 1: moves.append([path + 'U', [position[0], position[1]-1]])
        if hashed[1] in open_chr and position[1] != 4: moves.append([path + 'D', [position[0], position[1]+1]])
        if hashed[2] in open_chr and position[0] != 1: moves.append([path + 'L', [position[0]-1, position[1]]])
        if hashed[3] in open_chr and position[0] != 4: moves.append([path + 'R', [position[0]+1, position[1]]])
    return moves

def run():
    end_pos, ended = [4,4], False
    moves = valid_moves([['', start]])
    while not ended:
        moves = valid_moves(moves)
        for m in moves:
            if end_pos == m[-1]: 
                print(m[0])
                ended = True
def pt2():
    ended_paths, end_pos = [], [4,4]
    moves = valid_moves([['',start]])
    while len(moves) != 0:
        moves = valid_moves(moves)
        for m in moves:
            if end_pos == m[-1]:
                ended_paths.append(len(m[0]))
                moves.remove(m)
    print(max(ended_paths))
run()
pt2()