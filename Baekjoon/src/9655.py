N = int(input())
odd = False
while N > 0:
    if N >= 3:
        N -= 3
        if odd == False:
            odd = True
        else:
            odd = False
    else:
        N -= 1
        if odd == False:
            odd = True
        else:
            odd = False
print("SK" if odd else "CY")