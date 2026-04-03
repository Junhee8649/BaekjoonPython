import sys

input = sys.stdin.readline
N = int(input())
S = list(map(int, input().split()))

counts = {}
left, max_len = 0, 0

for right in range(N):
    counts[S[right]] = counts.get(S[right], 0) + 1

    # 과일 종류가 2개 초과면 줄이기
    while len(counts) > 2:
        counts[S[left]] -= 1
        if counts[S[left]] == 0:
            del counts[S[left]]
        left += 1

    # 최대 길이 갱신
    curr_len = right - left + 1
    max_len = max(max_len, curr_len)

print(max_len)