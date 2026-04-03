N = int(input())
X = list(map(int, input().split()))
X_temp = set(X)
X_temp = sorted(list(X_temp))
X_dic = dict()
for i in range(len(X_temp)):
    X_dic[X_temp[i]] = i

for j in X:
    print(X_dic[j], end=" ")