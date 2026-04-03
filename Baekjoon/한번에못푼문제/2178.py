from collections import deque

def solve_maze():
    n, m = map(int, input().split())
    
    # 미로 입력 받기 (붙어서 들어오므로 문자열로 처리)
    maze = []
    for _ in range(n):
        row = input().strip()  # 한 줄을 문자열로 받기
        maze.append(row)
    
    # BFS를 위한 준비
    queue = deque([(0, 0, 1)])  # (행, 열, 거리)
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    # 상하좌우 이동 방향
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
    
    while queue:
        row, col, distance = queue.popleft()
        
        # 목표 지점에 도달했으면 거리 반환
        if row == n - 1 and col == m - 1:
            return distance
        
        # 상하좌우로 이동
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            
            # 경계 체크 및 조건 확인
            if (0 <= new_row < n and 0 <= new_col < m and 
                not visited[new_row][new_col] and 
                maze[new_row][new_col] == '1'):
                
                visited[new_row][new_col] = True
                queue.append((new_row, new_col, distance + 1))

# 실행
print(solve_maze())