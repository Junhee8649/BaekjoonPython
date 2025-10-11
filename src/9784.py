T = int(input())
for j in range(T):
    n, P, Q = map(int, input().split())
    eggs = list(map(int, input().split()))
    eggs.sort()
    
    sum_eggs = 0
    egg_count = 0
    i = 0
    
    # while 루프는 그대로 사용하되,
    while i < n: # i가 달걀의 총 개수(n)보다 작을 동안에만 반복
        # 다음 달걀을 담을 수 있는지 미리 확인합니다.
        if egg_count < P and sum_eggs + eggs[i] <= Q:
            egg_count += 1
            sum_eggs += eggs[i]
            i += 1
        else:
            # 조건을 만족하지 못하면 더 이상 담을 수 없으므로 루프를 중단합니다.
            break
            
    print(f"Case {j+1}: {egg_count}")