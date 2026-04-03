Q = int(input())
problems = 0  

for _ in range(Q):
    event_type, count = map(int, input().split())
    
    if event_type == 1:
        problems += count
    elif event_type == 2:
        if problems < count:
            print("Adios")
            exit()
        problems -= count

# 모든 이벤트를 무사히 처리했으면
print("See you next month")