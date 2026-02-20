A, B = input().split()
small_A, small_B = 0, 0
big_A, big_B = 0, 0

A = A.replace('6', '5')
small_A = int(A)

A = A.replace('5', '6')
big_A = int(A)

B = B.replace('6', '5')
small_B = int(B)

B = B.replace('5', '6')
big_B = int(B)

print(small_A + small_B, big_A + big_B)