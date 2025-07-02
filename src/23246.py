n = int(input())
members = []

for i in range(n):
    b, p, q, r = map(int, input().split())
    score_mul = p*q*r
    score_sum = p+q+r
    members.append([score_mul, score_sum, b])

members.sort(key=lambda x: (x[0], x[1], x[2]))

for j in range(3):
    print(members[j][2], end=" ")
