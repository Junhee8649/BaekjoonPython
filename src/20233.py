a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input())

A_pay = a + ((T - 30) * x) * 21 if T > 30 else a
B_pay = b + ((T - 45) * y) * 21 if T > 45 else b

print(A_pay, B_pay)