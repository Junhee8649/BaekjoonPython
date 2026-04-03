while True:
    n = input()
    if n == '0':
        break
    
    width = 0
    width += (len(n) + 1)
    
    for digit in n:
        if digit == '1':
            width += 2
        elif digit == '0':
            width += 4
        else:
            width += 3
            
    print(width)