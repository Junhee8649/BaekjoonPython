H, W = map(int, input().split())
block = list(map(int, input().split()))

count = 0
for i in range(1,W):
    count += abs(block[i] - min(max(block[:i+1]), max(block[i:])))
                
print(count)