n = int(input())
if n >= 0:
    print(len(bin(n))-2)
else:
    # 문제에서 연속된 0은 저장 안하니까 음수는 다 32
    print(32)