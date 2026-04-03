length = int(input())
name = input()
score = 0
for i in name:
    score += ord(i) - 64
print(score)