N = int(input())
count = (2*N + 1) ** 2  # a = 0인 경우

# a ≠ 0인 경우: a + b + c = 1
for a in range(-N, N+1):
    if a != 0:
        k = 1 - a  # b + c = k
        
        # b + c = k인 유효한 (b, c) 쌍의 개수
        b_min = max(-N, k - N)
        b_max = min(N, k + N)
        
        if b_min <= b_max:
            count += b_max - b_min + 1

print(count)