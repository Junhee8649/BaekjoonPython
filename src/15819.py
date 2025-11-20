N, I = map(int, input().split())
words = []
for _ in range(N):
    words.append(input())
words.sort()
print(words[I-1])