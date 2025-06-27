P1_x, P1_y = map(int, input().split())
P2_x, P2_y = map(int, input().split())
P3_x, P3_y = map(int, input().split())

cross_product = (P2_x - P1_x) * (P3_y - P2_y) - (P2_y - P1_y) * (P3_x - P2_x)

if cross_product > 0:
    print(1)    # 반시계 방향
elif cross_product < 0:
    print(-1)   # 시계 방향
else:
    print(0)    # 일직선