from math import inf


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
home = []
chicken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append([i+1, j+1])
        elif city[i][j] == 2:
            chicken.append([i+1, j+1])
answer = inf
temp_chicken = []
def distance(list1,list2):
    return abs(list1[1]-list2[1]) + abs(list1[0]-list2[0])

def dfs(depth, start):
    global answer
    if depth == M:
        result = 0
        for i in home:
            result += min(distance(tc, i) for tc in temp_chicken)
        answer = min(answer, result)
        return
    for i in range(start, len(chicken)):
        temp_chicken.append(chicken[i])
        dfs(depth+1, i+1)
        temp_chicken.remove(chicken[i])
dfs(0,0)
print(answer)