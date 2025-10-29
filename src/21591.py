w_c, h_c, w_s, h_s = map(int, input().split())

condition_width = (w_s + 2) <= w_c
condition_height = (h_s + 2) <= h_c

if condition_width and condition_height:
    print(1)
else:
    print(0)