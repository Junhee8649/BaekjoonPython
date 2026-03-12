N = int(input())
word = "SciComLove"
N = N % 10
for i in range(N):
    word = word[1:] + word[0]
print(word)