puzzle_input = '^.....^.^^^^^.^..^^.^.......^^..^^^..^^^^..^.^^.^.^....^^...^^.^^.^...^^.^^^^..^^.....^.^...^.^.^^.^'
rows = 40
def next_row(row):
    new_row,  walls = '', '.'+ row + '.'
    for i in range(1, len(walls)-1):
        x, traps = walls[i-1:i+2], ['^^.', '.^^','^..','..^']
        if x in traps: new_row += '^'
        else: new_row += '.'
    return new_row
def run(row, row_ct):
    grid = [row]
    while len(grid) != row_ct:
        row = next_row(row)
        grid.append(row)
    print (''.join(grid).count('.'))

run(puzzle_input,rows)
run(puzzle_input,400000)