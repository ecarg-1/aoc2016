import re, numpy as np
with open('input.txt','r') as f:
    directions = [re.sub('rotate ', '', line.strip('\n')).split(' ') for line in f.readlines()]
    f.close()
matrix = np.zeros([6, 50])
def rect(w, l, mat):
    mat[0:l, 0:w] = 1
def rotate_row(row, amount, mat):
    mat[row, :amount], mat[row, amount:] = mat[row, -amount:].copy(), mat[row, :-amount].copy()
def rotate_col(col, amount, mat):
    mat[:amount, col], mat[amount:,col]  = mat[-amount:,col].copy(), mat[:-amount, col].copy()
for i in directions:
    match i[0]:
        case 'row': rotate_row(int(i[1][2:]), int(i[-1]), matrix)
        case 'column': rotate_col(int(i[1][2:]), int(i[-1]), matrix)
        case 'rect': rect(int(i[1].split('x')[0]), int(i[1].split('x')[-1]), matrix)
print(np.count_nonzero(matrix))
for line in matrix:
    for c in range(len(line)):
        if c%5==0 and c!=0: print('\t', end='')
        print('*' if line[c]==1 else ' ', end='')
    print()