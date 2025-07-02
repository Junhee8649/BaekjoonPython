N, M = map(int, input().split())
listen = set()
see = set()

for i in range(N):
    listen.add(input())
for j in range(M):
    see.add(input())

count = 0
count_list = []
for k in listen:
    if k in see:
        count += 1
        count_list.append(k)
    
count_list.sort()    
print(count)
for i in count_list:
    print(i)