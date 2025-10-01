N = int(input())
words = []
for _ in range(N):
    word = input()
    reverse = word[::-1]
    if reverse == word or reverse in words:
        print(len(word), word[len(word)//2])
    words.append(word)