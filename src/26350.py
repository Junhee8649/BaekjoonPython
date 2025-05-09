n = int(input())
for i in range(n):
    d_set = list(map(int, input().split()))
    is_two_times = True
    for j in range(1, d_set[0]):
        if d_set[j+1] < d_set[j] * 2: is_two_times = False

    print(f"Denominations: ", end="")
    print(*d_set[1:])

    if is_two_times == True: 
        print("Good coin denominations!") 
    else: 
        print("Bad coin denominations!")
    print("")
