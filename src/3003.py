chess = [1,1,2,2,2,8]
now_chess = list(map(int, input().split()))

for i in range(len(chess)):
    print(chess[i]-now_chess[i], end=" ")