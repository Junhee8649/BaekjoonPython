nums = []
for _ in range(5):
    nums.append(int(input()))
nums.sort()
avg = sum(nums) // 5
middle = nums[2]
print(avg)
print(middle)