n = int(input())
sticks = list(map(int, input().split()))
longest_stick = sum(sticks)
cost = 0
for stick in sticks:
    longest_stick -= stick
    cost += stick * longest_stick
print(cost)