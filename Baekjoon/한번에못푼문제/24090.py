import sys

def partition(A, p, r):
    global swap_count, K, kth_swap
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            swap_count += 1
            if swap_count == K:
                kth_swap = (A[i], A[j])

    if i + 1 != r:
        A[i + 1], A[r] = A[r], A[i + 1]
        swap_count += 1
        if swap_count == K:
            kth_swap = (A[i + 1], A[r])
    return i + 1

# 재귀 대신 반복문을 사용하는 quick_sort
def quick_sort_iterative(A, p, r):
    global kth_swap
    
    # 정렬할 범위를 저장할 스택을 만듭니다.
    stack = [(p, r)]
    
    # 스택이 비어있지 않은 동안 반복
    while stack:
        # 정렬할 범위를 스택에서 꺼냅니다.
        p, r = stack.pop()
        
        # (재귀 함수의 'if p < r'과 조기 종료 조건)
        if p < r and not kth_swap:
            # 파티션을 수행합니다.
            q = partition(A, p, r)
            
            # 두 개의 하위 범위를 다시 스택에 넣습니다.
            # (재귀 호출 대신)
            stack.append((p, q - 1))
            stack.append((q + 1, r))

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
swap_count = 0
kth_swap = None

# 재귀 함수 대신 새로 만든 반복문 함수를 호출합니다.
quick_sort_iterative(A, 0, N - 1)

if kth_swap:
    print(min(kth_swap), max(kth_swap))
else:
    print(-1)