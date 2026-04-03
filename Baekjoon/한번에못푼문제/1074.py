def solve(n, r, c):
    """
    n: 현재 정사각형의 한 변의 크기 2^n
    r: 목표 행
    c: 목표 열
    반환값: (r, c)의 방문 순서
    """

    # --- 1. 기저 조건 (Base Case) ---
    # n=0 이면 (1x1 크기) 더 이상 쪼갤 수 없음
    # 해당 칸의 순서는 0 (누적된 값을 반환)
    if n == 0:
        return 0

    # --- 2. 분할 (Divide) ---
    # 현재 2^n 크기를 2^(n-1) 크기의 4개 사분면으로 쪼갬
    half = 2**(n - 1)
    
    # 한 사분면이 가지는 칸의 총 개수 (넓이)
    quadrant_size = half * half  # (2**(n-1)) * (2**(n-1))

    # --- 3. 정복 (Conquer) & 결합 (Combine) ---
    
    # 1사분면 (왼쪽 위)
    if r < half and c < half:
        # 1사분면에 속하면, 0을 더하고 
        # n-1 크기의 1사분면 문제로 재귀 호출
        # 좌표 (r, c)는 그대로 사용
        return solve(n - 1, r, c)
    
    # 2사분면 (오른쪽 위)
    elif r < half and c >= half:
        # 2사분면에 속하면, 1사분면의 넓이(quadrant_size)를 더함
        # n-1 크기의 2사분면 문제로 재귀 호출
        # 열 좌표를 (c - half)로 바꿔서 넘김
        return (1 * quadrant_size) + solve(n - 1, r, c - half)

    # 3사분면 (왼쪽 아래)
    elif r >= half and c < half:
        # 3사분면에 속하면, 1, 2사분면의 넓이(2 * quadrant_size)를 더함
        # n-1 크기의 3사분면 문제로 재귀 호출
        # 행 좌표를 (r - half)로 바꿔서 넘김
        return (2 * quadrant_size) + solve(n - 1, r - half, c)

    # 4사분면 (오른쪽 아래)
    else: # r >= half and c >= half
        # 4사분면에 속하면, 1, 2, 3사분면의 넓이(3 * quadrant_size)를 더함
        # n-1 크기의 4사분면 문제로 재귀 호출
        # 행, 열 좌표를 (r - half), (c - half)로 바꿔서 넘김
        return (3 * quadrant_size) + solve(n - 1, r - half, c - half)


# --- 4. 입력 및 실행 ---
# N, r, c 입력 받기
N, r, c = map(int, input().split())

# 함수 호출 및 결과 출력
result = solve(N, r, c)
print(result)