from itertools import count


n, d = map(int, input().split())
numbers = ""
for i in range(1, n+1):
    numbers += str(i)
print(numbers.count(str(d)))