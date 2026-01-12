T = int(input())
for _ in range(T):
    A, B = input().split()
    A_list = []
    B_list = []
    for i in A:
        A_list.append(i)
    for j in B:
        B_list.append(j)
    A_list.sort()
    B_list.sort()
    if A_list == B_list:
        print(f"{A} & {B} are anagrams.")
    else:
        print(f"{A} & {B} are NOT anagrams.")