from collections import deque

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    deque_list = list(map(int, input().split()))
    printer = deque(deque_list)
    count = 0
    times = int((N * (N + 1)) / 2)
    
    for j in range(times):
        if printer[0] == max(printer):
            count += 1
            if M == 0: 
                print(count)
                break
            printer.popleft()
        else:
            printer.rotate(-1)

        M = M - 1 if M != 0 else len(printer) - 1