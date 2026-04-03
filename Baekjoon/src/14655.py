N = int(input())
first_round = list(map(int, input().split()))
second_round = list(map(int, input().split()))
sum = 0
for num in first_round:
    sum += abs(num)
for num in second_round:
    sum += abs(num)
print(sum)