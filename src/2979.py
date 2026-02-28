A, B, C = map(int, input().split())
car1_in, car1_out = map(int, input().split())
car2_in, car2_out = map(int, input().split())
car3_in, car3_out = map(int, input().split())
now_car, payment = 0, 0
is_car1, is_car2, is_car3 = False, False, False

last_time = max(car1_out, car2_out, car3_out)

for i in range(1, last_time+1):
    if car1_in <= i and car1_out > i:
        if not is_car1:
            now_car += 1
            is_car1 = True
    else:
        if is_car1:
            now_car -= 1
            is_car1 = False

    if car2_in <= i and car2_out > i:
        if not is_car2:
            now_car += 1
            is_car2 = True
    else:
        if is_car2:
            now_car -= 1
            is_car2 = False

    if car3_in <= i and car3_out > i:
        if not is_car3:
            now_car += 1
            is_car3 = True
    else:
        if is_car3:
            now_car -= 1
            is_car3 = False

    if now_car == 1:
        payment += A
    elif now_car == 2:
        payment += 2*B
    elif now_car == 3:
        payment += 3*C
print(payment)