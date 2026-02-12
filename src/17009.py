A3 = int(input()) * 3
A2 = int(input()) * 2
A1 = int(input())
B3 = int(input()) * 3
B2 = int(input()) * 2
B1 = int(input())

A = A3 + A2 + A1
B = B3 + B2 + B1

if A > B:
    print("A")
elif B > A:
    print("B")
else:
    print("T")