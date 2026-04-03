from collections import deque


N = int(input())
K = int(input())
apples = []
for i in range(K):
    apples.append(list(map(int, input().split())))
L = int(input())
snake_direction = []
for i in range(L):
    X, C = input().split()
    snake_direction.append([int(X), C])
# 동 남 서 북
dx = [1,0,-1,0]
dy = [0,1,0,-1]
snake = deque()
snake.append([1,1])
snake_direction_num = 0
time = 0
time_direction_pivot = 0

while True: 
    now_head_y, now_head_x = snake[-1][0], snake[-1][1]
    next_head_x = now_head_x + dx[snake_direction_num]
    next_head_y = now_head_y + dy[snake_direction_num]
    if [next_head_y, next_head_x] in snake or next_head_x > N or next_head_x <= 0 or next_head_y > N or next_head_y <= 0:
        break
    snake.append([next_head_y, next_head_x])
    if snake[-1] not in apples:
        snake.popleft()
    else:
        apples.remove(snake[-1])
    time += 1
    if time_direction_pivot < len(snake_direction) and snake_direction[time_direction_pivot][0] == time:
        if snake_direction[time_direction_pivot][1] == 'L':
            snake_direction_num = (snake_direction_num - 1) % 4
        elif snake_direction[time_direction_pivot][1] == 'D':
            snake_direction_num = (snake_direction_num + 1) % 4
        time_direction_pivot += 1
    
print(time + 1)