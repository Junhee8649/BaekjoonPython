T = int(input())
for _ in range(T):
    M, choose = input().split()
    question = input().split()
    answer = []

    if choose == 'C':
        for char in question:
            answer.append(ord(char) - 64)
    else:
        for num in question:
            answer.append(chr(int(num) + 64))

    print(*answer)