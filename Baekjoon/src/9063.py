N = int(input())
x_list, y_list = [], []
for i in range(N):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
    
a = max(x_list) - min(x_list)
b = max(y_list) - min(y_list)

if N == 1:
    print(0)
else:
    print(a*b)