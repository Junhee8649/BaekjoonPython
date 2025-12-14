from collections import Counter


N = int(input())
students = list(map(int, input().split()))
temp = Counter(students)
max_people = 0

for i in temp.values():
    if i >= 2:
        max_people += 2
    else:
        max_people += i
print(max_people)