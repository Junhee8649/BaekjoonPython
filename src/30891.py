def safe_rice(X,Y,x,y,R):
    if (X-x)**2 + (Y-y)**2 <= R**2:
        return True
    else:
        return False
    
max_rice = 0
rice_list = []
wok = [0,0]
N, R = map(int, input().split())
for _ in range(N):
    rice_list.append(list(map(int, input().split())))

for X in range(-100, 101):
    for Y in range(-100, 101):
        temp = 0
        for coordinate in rice_list:
            if safe_rice(X,Y,coordinate[0],coordinate[1],R):
                temp += 1
        if max_rice < temp:
            max_rice = temp
            wok[0] = X
            wok[1] = Y
print(wok[0], wok[1])