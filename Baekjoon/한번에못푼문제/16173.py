n = int(input())
game_map = []
for _ in range(n):
    game_map.append(list(map(int, input().split())))
visited = [[False] * n for _ in range(n)]

def dfs(x,y):
    if x == n-1 and y == n-1:
        return True
    visited[x][y] = True
    jump = game_map[x][y]

    if jump == 0:
        return False
    if y + jump < n and not visited[x][y + jump]:
        if dfs(x, y + jump):
            return True
    if x + jump < n and not visited[x + jump][y]:
        if dfs(x + jump, y):
            return True
    return False
    
if dfs(0, 0):
    print("HaruHaru")
else:
    print("Hing")