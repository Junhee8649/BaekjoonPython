N = int(input())
while N != 0:
    words = []
    for _ in range(N):
        word = input()
        small_word = word.lower()
        words.append([small_word,word])
    words.sort()
    print(words[0][1])
    N = int(input())