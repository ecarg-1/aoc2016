import numpy as np, collections
with open('input.txt','r') as f:
    words = [line.strip('\n') for line in f.readlines()]
    f.close()
cols, rows = len(words[0]), len(words)
matrix = np.zeros([rows,cols])
for r in range(rows):
    for c in range(cols):
        matrix[r][c] = ord(words[r][c])
matrix = np.transpose(matrix)
message1, message2 = '', ''
for i in matrix:
    message1 += chr(int(collections.Counter(i).most_common()[0][0]))
    message2 += chr(int(collections.Counter(i).most_common()[-1][0]))
print(message1, message2)
    
