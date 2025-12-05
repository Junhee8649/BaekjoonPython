int(input())
nums = list(set(map(int, input().split())))
nums.sort()
for i in nums:
    print(i, end=" ")