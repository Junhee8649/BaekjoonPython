def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

N = int(input())
for _ in range(N):
    nums = list(map(int, input().split()))
    max_num = 0
    i = 0
    while i < len(nums) - 1:
        new_nums = nums[i+1:]
        for num in new_nums:
            max_num = max(max_num, gcd(nums[i], num))
        i += 1
    print(max_num)