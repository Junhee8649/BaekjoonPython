import math

T = int(input())
    
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
        
    # 두 원의 중심 사이의 거리
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
    # 경우별 분석
    if distance == 0:  # 두 원의 중심이 같음
        if r1 == r2:  # 완전히 같은 원
            print(-1)  # 무한대
        else:  # 중심은 같지만 반지름이 다름
            print(0)  # 만나지 않음
        
    elif distance > r1 + r2:  # 너무 멀리 떨어져 있음
        print(0)
        
    elif distance == r1 + r2:  # 외접
        print(1)
        
    elif distance == abs(r1 - r2):  # 내접
        print(1)
        
    elif distance < abs(r1 - r2):  # 한 원이 다른 원 내부에 포함
        print(0)
        
    else:  # abs(r1-r2) < distance < r1+r2
        print(2)  # 두 점에서 교차