def max_cherry_group_sum(N, A):
    max_sum = 0
    
    # i, j, k는 3개의 분할 지점을 나타냄
    # 분할 후의 그룹: [0...i], [i+1...j], [j+1...k], [k+1...N-1]
    for i in range(N-3):
        for j in range(i+1, N-2):
            for k in range(j+1, N-1):
                # 각 그룹의 곱 계산
                p1 = product(A, 0, i)
                p2 = product(A, i+1, j)
                p3 = product(A, j+1, k)
                p4 = product(A, k+1, N-1)
                
                # 현재 분할의 합 계산
                current_sum = p1 + p2 + p3 + p4
                max_sum = max(max_sum, current_sum)
    
    return max_sum

def product(arr, start, end):
    """배열의 start부터 end까지의 요소들의 곱을 반환"""
    prod = 1
    for i in range(start, end+1):
        prod *= arr[i]
    return prod

n = int(input())
blossom = list(map(int, input().split()))
print(max_cherry_group_sum(n, blossom))