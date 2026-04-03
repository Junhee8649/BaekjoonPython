score = []
for i in range(8):
    score.append(int(input()))
new_score = sorted(score, reverse=True)
print(sum(new_score[:5]))
temp = []
for i in range(5):
    temp.append(score.index(new_score[i])+1)
temp.sort()
for j in temp:
    print(j, end=" ")