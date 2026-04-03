N = int(input())
seats = input()
count = 1

for i in seats:
    if i == 'S':
        count += 1
    else:
        count += 0.5
if count <= N:
    print(int(count))
else:
    print(N)