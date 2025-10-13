N = int(input())
rope = []
for _ in range(N):
    rope.append(int(input()))
rope.sort()
max = 0
for i in range(N):
    max = rope[i] * (N-i) if max < rope[i] * (N-i) else max
print(max)