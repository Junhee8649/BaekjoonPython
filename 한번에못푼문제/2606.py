def dfs(graph, start, visited):
    visited[start] = True
    count = 1

    for neighbor in graph[start]:
        if not visited[neighbor]:
            count += dfs(graph, neighbor, visited)
    return count

computer = int(input())
connect = int(input())
graph = [[] for _ in range(computer + 1)]

for _ in range(connect):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (computer + 1)

print(dfs(graph, 1, visited) - 1)