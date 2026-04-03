import sys

input = sys.stdin.readline
N = int(input())
people = 0
for _ in range(N):
    type = input().split()
    type_count = int(type[2])
    if type[1] == "IN":
        people += type_count
    else:
        people -= type_count
if people == 0:
    print("NO STRAGGLERS")
else:
    print(people)