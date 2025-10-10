N, M = map(int, input().split())
sum = 0
puzzle = []
for i in range(N):
    puzzle.append(input().strip())
for j in range(N-1):
    for k in range(M):
        if (puzzle[j][k] == "X" and puzzle[j+1][k] == "Y") or (puzzle[j][k] == "Y" and puzzle[j+1][k] == "X"):
            sum += 1
for j in range(N):
    for k in range(M-1):
        if (puzzle[j][k] == "X" and puzzle[j][k+1] == "Y") or (puzzle[j][k] == "Y" and puzzle[j][k+1] == "X"):
            sum += 1
print(sum)