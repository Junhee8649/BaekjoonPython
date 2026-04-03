from collections import Counter
import sys

N, K = map(int, sys.stdin.readline().split())
present = list(map(int, sys.stdin.readline().split()))
present_box = list(map(int, sys.stdin.readline().split()))
people = list(map(int, sys.stdin.readline().split()))

counter = Counter(present_box)
counter.subtract(people)

box = max(+counter)
answer = max(i for i in present if i <= box)

print(answer)