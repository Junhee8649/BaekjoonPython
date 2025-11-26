from collections import deque

N = int(input())
card = deque(i for i in range(1,N+1))
throw = []
for i in range(N-1):
    throw.append(card.popleft())
    temp = card.popleft()
    card.append(temp)
throw.append(card.popleft())
for i in throw:
    print(i, end=" ")