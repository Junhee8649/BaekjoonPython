N, K = map(int, input().split())
olympic = []
for _ in range(N):
    olympic.append(list(map(int, input().split())))

# 메달 기준 내림차순 정렬
olympic.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

ranks = [0] * N  # 등수 저장 리스트
rank = 1
ranks[0] = rank
prev_medals = olympic[0][1:4]

for i in range(1, N):
    current_medals = olympic[i][1:4]
    if current_medals == prev_medals:
        ranks[i] = rank  # 동점일 경우 같은 등수
    else:
        rank = i + 1
        ranks[i] = rank
        prev_medals = current_medals

# K 국가의 등수 출력
for i in range(N):
    if olympic[i][0] == K:
        print(ranks[i])
        break