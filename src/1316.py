N = int(input())
count = 0
for _ in range(N):
    word = input()
    i = 0
    while i < len(word) -1:
        if word[i] == word[i+1]:
            word = word[0:i+1]+ word[i+2:]
        else:
            i += 1
    filter = []
    answer = True
    for letter in word:
        if letter in filter:
            answer = False
            break
        filter.append(letter)
    if answer: 
        count += 1
print(count)