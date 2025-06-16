N = int(input())
count = 0
student = [' '] * N

for i in range(N):
    student[i] = input()

for j in range(N):
    answer = input()
    if student[j] == answer:
        count += 1

print(count)