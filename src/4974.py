while True:
    n = int(input())
    if n == 0:
        break
    score = []
    for i in range(n):
        score.append(int(input()))
    score.sort()
    size = len(score)
    print(int(sum(score[1:size-1]) / (size-2)))