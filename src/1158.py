N, K = map(int, input().split())
circle = [i for i in range(1,N+1)]
new_circle = []
temp = -1
for num in range(N):
    temp = (temp + K) % len(circle)
    new_circle.append(circle[temp])
    del circle[temp]
    if len(circle) != 0:
        temp = (temp - 1) % len(circle)
    else:
        temp = (temp - 1)

print("<", end="")
for i in new_circle:
    if i == new_circle[-1]:
        print(f"{i}>")
    else:
        print(f"{i},", end=" ")