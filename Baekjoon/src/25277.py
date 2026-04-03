N = int(input())
sentence = input().split()
temp = ["he", "him", "she", "her"]
count = 0

for word in sentence:
    if word in temp:
        count += 1
print(count)