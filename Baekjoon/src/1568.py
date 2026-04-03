N = int(input())
sing = 1
time = 0
while N > 0:
    N -= sing
    sing += 1
    time += 1
    if sing > N:
        sing = 1
print(time)