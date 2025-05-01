from math import sqrt
from decimal import Decimal, getcontext

getcontext().prec = 28  # 정밀도 설정

n, k = map(int, input().split())
people = list(map(Decimal, input().split()))  # Decimal 사용

# 누적 합과 제곱 누적 합 미리 계산
prefix_sum = [Decimal(0)] * (n + 1)
prefix_sum_sq = [Decimal(0)] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + people[i]
    prefix_sum_sq[i + 1] = prefix_sum_sq[i] + people[i] ** 2

min_std = Decimal('inf')
# k개 이상의 모든 경우를 고려
for length in range(k, n+1):
    for i in range(n-length+1):
        # 구간의 합과 제곱합을 O(1)로 계산
        sum_val = prefix_sum[i + length] - prefix_sum[i]
        sum_sq = prefix_sum_sq[i + length] - prefix_sum_sq[i]
        
        # 평균
        m = sum_val / length
        
        # 분산: E[X²] - (E[X])² 공식 사용
        variance = sum_sq / length - m * m
        
        # 부동소수점 오차 처리
        if variance < 0:
            variance = Decimal(0)
        
        # 표준편차
        std = variance.sqrt()
        
        min_std = min(min_std, std)

print(min_std)