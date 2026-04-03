def tetromino_one(paper,N,M):
    max_sum = 0
    for i in range(N):
        for j in range(M-3):
            max_sum = max(max_sum, sum(paper[i][j:j+4]))
    for i in range(N-3):
        for j in range(M):
            max_sum = max(max_sum, paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+3][j])
    return max_sum
def tetromino_two(paper,N,M):
    max_sum = 0
    for i in range(N-1):
        for j in range(M-1):
            max_sum = max(max_sum, sum(paper[i][j:j+2]) + sum(paper[i+1][j:j+2]))
    return max_sum
def tetromino_three(paper,N,M):
    max_sum = 0
    for i in range(N-2):
        for j in range(M-1):
            max_sum = max(max_sum, paper[i][j] + paper[i+1][j] + sum(paper[i+2][j:j+2]), sum(paper[i+2][j:j+2]) + paper[i][j+1] + paper[i+1][j+1], sum(paper[i][j:j+2]) + paper[i+1][j] + paper[i+2][j], sum(paper[i][j:j+2]) + paper[i+1][j+1] + paper[i+2][j+1])
    for i in range(N-1):
        for j in range(M-2):
            max_sum = max(max_sum, sum(paper[i][j:j+3]) + paper[i+1][j], sum(paper[i][j:j+3]) + paper[i+1][j+2], paper[i][j+2] + sum(paper[i+1][j:j+3]), paper[i][j] + sum(paper[i+1][j:j+3]))
    return max_sum
def tetromino_four(paper,N,M):
    max_sum = 0
    for i in range(N-2):
        for j in range(M-1):
            max_sum = max(max_sum, paper[i][j] + sum(paper[i+1][j:j+2]) + paper[i+2][j+1], paper[i][j+1] + sum(paper[i+1][j:j+2]) + paper[i+2][j])
    for i in range(N-1):
        for j in range(M-2):
            max_sum = max(max_sum, sum(paper[i][j+1:j+3]) + sum(paper[i+1][j:j+2]), sum(paper[i][j:j+2]) + sum(paper[i+1][j+1:j+3]))
    return max_sum
def tetromino_five(paper,N,M):
    max_sum = 0
    for i in range(N-1):
        for j in range(M-2):
            max_sum = max(max_sum, sum(paper[i][j:j+3]) + paper[i+1][j+1], paper[i][j+1] + sum(paper[i+1][j:j+3]))
    for i in range(N-2):
        for j in range(M-1):
            max_sum = max(max_sum, paper[i][j+1] + sum(paper[i+1][j:j+2]) + paper[i+2][j+1], paper[i][j] + sum(paper[i+1][j:j+2]) + paper[i+2][j])
    return max_sum

N, M = map(int, input().split())
paper = []

for col in range(N):
    paper.append(list(map(int, input().split())))

print(max(tetromino_one(paper,N,M), tetromino_two(paper,N,M), tetromino_three(paper,N,M), tetromino_four(paper,N,M), tetromino_five(paper,N,M)))