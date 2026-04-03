import sys


n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
x = int(input())

nums.sort()
count = 0
left, right = 0, n - 1

while left < right:
    temp_sum = nums[left] + nums[right]
    if temp_sum == x:
        count += 1
        left += 1  
        right -= 1 
    elif temp_sum < x:
        left += 1   
    else: 
        right -= 1  
print(count)