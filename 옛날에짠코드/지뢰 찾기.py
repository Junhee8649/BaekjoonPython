def Search(a,b):
    count = 0
    for x in range(a-1,a+2):
        for y in range(b-1,b+2):
            if matrix[x][y] == '*':
                count += 1
    return count

col,row = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))

for j in range(row):
    matrix[j].insert(0,'.')
    matrix[j].append('.')
L = ['.']*(col+2)
matrix.insert(0,L)
matrix.append(L)

for a in range(1,row+1):
    for b in range(1,col+1):
        if matrix[a][b] == '*':
            continue
        matrix[a][b] = Search(a,b)

for a in range(1,row+1):
    for b in range(1,col+1):
        print(matrix[a][b],end='')
    print()