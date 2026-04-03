from math import gcd


first_dice = list(map(int, input().split()))
second_dice = list(map(int, input().split()))
dice_num = 6
count = 0
denominator = 36

for i in range(dice_num):
    for j in range(dice_num):
        if first_dice[i] > second_dice[j]:
            count += 1

gcd_num = gcd(denominator, count)
if denominator % gcd_num == 0:
    denominator //= gcd_num
    count //= gcd_num

print(f"{count}/{denominator}")