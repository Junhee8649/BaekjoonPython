n = int(input())
coding = list(map(int, input().split()))
coding.sort()
answer = float('inf')

for i in range(n):
    answer = min(answer, coding[i] + coding[-(i+1)])
print(answer)