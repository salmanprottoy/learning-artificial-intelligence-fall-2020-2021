#puzzle2d = [[7, 1, 2], [5, ' ', 4], [8, 3, 6]]
puzzle2d = [[13, 10, 11, 6], [5, 7, 4, 8], [1, 12, 14, 9],[3, 15, 2, ' ']]
dim = len(puzzle2d)
puzzle = []
blankAt = []

for i in  range(0, dim):
    for j in range(0, dim):
        if puzzle2d[i][j] == ' ':
            blankAt = [i, j]
            continue
        else:
            puzzle.append(puzzle2d[i][j])

inversionVal = 0
dim1d = len(puzzle)

k = 0
while k < dim1d:
    for j in range(k, dim1d):
        if puzzle[k] > puzzle[j]:
            inversionVal += 1
    k += 1

blankRow = dim - (blankAt[0])
print(blankRow)
print(inversionVal)
print(dim)

if dim%2 != 0:
    if inversionVal%2 == 0:
        print("Puzzle is Solvable")
elif dim%2 == 0 and blankRow%2 != 0:
    if inversionVal%2 == 0:
        print("Puzzle is Solvable")
elif dim%2 == 0 and blankRow%2 == 0:
    if inversionVal%2 != 0:
        print("Puzzle is Solvable")
else:
    print("Puzzle is NOT Solvable")
