def score_choose(sub1, sub2, l):
    if l >= sub2:
        return 140
    elif l >= sub1:
        return 100
    else:
        return 0

n, l, k = map(int, input().split())
temp_list = [0] * n
for i in range(n):
    sub1, sub2 = map(int, input().split())
    temp_list[i] = score_choose(sub1, sub2, l)
temp_list.sort()
print(sum(temp_list[-k:]) if k!= 0 else 0)