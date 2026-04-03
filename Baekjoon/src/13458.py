N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
people = 0

for i in A:
    i -= B
    people += 1
    if i > 0:
        bu = i // C
        if i % C == 0:
            people += bu
        else:
            people += (bu + 1)
print(people)