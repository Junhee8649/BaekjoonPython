S = input()
score = 1
temp = 1
for word in range(len(S)-1):
    if S[word+1] > S[word]:
        temp += 1
    else:
        temp = 1
    score += temp
print(score)