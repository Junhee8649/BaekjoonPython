N, M, K = map(int, input().split())
fireball_information = [list(map(int, input().split())) for _ in range(M)]
fireballs_msd = [[[-1,-1,-1]] * N for _ in range(N)]
for i in fireball_information:
    r,c,m,s,d = i
    r, c = r-1, c-1
    fireballs_msd[r][c] = [m,s,d]
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def move_fireballs():
    # 1. 동시성 보장을 위해 임시 맵(temp_msd)을 생성하여 이동 결과를 저장
    temp_msd = [[[-1,-1,-1]] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if fireballs_msd[i][j] != [-1,-1,-1]:
                sr,sc = i,j
                for k in range(0, len(fireballs_msd[i][j]), 3):
                    m, s, d = fireballs_msd[i][j][k], fireballs_msd[i][j][k+1], fireballs_msd[i][j][k+2]
                    nr, nc = (sr + s*dr[d]) % N, (sc + s*dc[d]) % N
                    if temp_msd[nr][nc] == [-1,-1,-1]:
                        temp_msd[nr][nc] = [m,s,d]
                    else:
                        temp_msd[nr][nc] += [m,s,d]
    # 2. 이동이 모두 끝나면 원본 맵을 temp_msd로 교체합니다. 
    # (기존의 복잡했던 원본 삭제 로직이 필요 없어집니다!)
    for i in range(N):
        for j in range(N):
            fireballs_msd[i][j] = temp_msd[i][j]
        
# fireballs는 [1,2,3,1,3,4] 이런 느낌
def sum_fireballs(fireballs, sr, sc, temp_sum):
    sum_m, sum_s, fireballs_count, all_d = 0, 0, len(fireballs) // 3, []
    for i in range(0, len(fireballs), 3):
        i_m, i_s, i_d = fireballs[i], fireballs[i+1], fireballs[i+2] 
        sum_m += i_m
        sum_s += i_s
        all_d.append(i_d)
    seperate_m = sum_m // 5
    seperate_s = sum_s // fireballs_count
    odd, even = [], []
    for d in all_d:
        if d % 2 == 1:
            odd.append(d)
        elif d % 2 == 0:
            even.append(d)
    # 3. [버그 수정] 모인 파이어볼의 개수는 4개가 아닐 수 있으므로 fireballs_count와 비교
    if len(odd) == fireballs_count or len(even) == fireballs_count:
        new_d = [0,2,4,6]
    else:
        new_d = [1,3,5,7]
    if seperate_m > 0:
        for d in new_d:
            # 4. [버그 수정] 분열된 파이어볼은 이동하지 않고 제자리(sr, sc)에 기록해야 합니다.
            if temp_sum[sr][sc] == [-1,-1,-1]: 
                temp_sum[sr][sc] = [seperate_m, seperate_s, d]
            else:
                temp_sum[sr][sc] += [seperate_m, seperate_s, d]
    fireballs_msd[sr][sc] = [-1,-1,-1]
            
    

def calculate_fireballs_amount():
    answer = 0
    for i in range(N):
        for j in range(N):
            grid = fireballs_msd[i][j]
            if grid != [-1,-1,-1]:
                for k in range(0, len(grid), 3):
                    answer += grid[k]
    return answer

for _ in range(K):
    move_fireballs()
    temp_sum = [[[-1,-1,-1]] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if len(fireballs_msd[i][j]) > 3:
                sum_fireballs(fireballs_msd[i][j], i, j, temp_sum)
    for i in range(N):
        for j in range(N):
            if temp_sum[i][j] != [-1,-1,-1]:
                if fireballs_msd[i][j] == [-1,-1,-1]:
                    fireballs_msd[i][j] = temp_sum[i][j]
                else:
                    fireballs_msd[i][j] += temp_sum[i][j]


answer = calculate_fireballs_amount()
print(answer)