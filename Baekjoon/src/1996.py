N = int(input())
# 리스트 컴프리헨션 잘 쓰자 
# game_map = [[0] * (N+2)] * (N+2) 이렇게 만들면 game_map[1][2] = '*' 하면 모든 행의 2번째 요소가 '*'로 바뀜
game_map = [[0] * (N+2) for _ in range(N+2)]
for i in range(1,N+1):
    temp = input()
    for j in range(1,N+1):
        if temp[j-1] != '.':
            game_map[i][j] = '*'
            for a in range(i-1,i+2):
                for b in range(j-1,j+2):
                    if game_map[a][b] != '*':
                        game_map[a][b] += int(temp[j-1])

for i in range(1,N+1):
    for j in range(1,N+1):
        if game_map[i][j] != '*':
            print(game_map[i][j] if int(game_map[i][j]) < 10 else 'M', end="")
        else:
            print(game_map[i][j], end="")
    print()