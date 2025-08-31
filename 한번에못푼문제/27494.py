def can_make_2023(num_str):
    """주어진 숫자 문자열에서 2023을 순서대로 만들 수 있는지 확인"""
    target = "2023"
    target_idx = 0
    
    for char in num_str:
        # 현재 찾고 있는 숫자와 일치하면 다음 숫자를 찾도록 진행
        if target_idx < len(target) and char == target[target_idx]:
            target_idx += 1
    
    # 모든 숫자(2, 0, 2, 3)를 찾았는지 확인
    return target_idx == len(target)

N = int(input())
count = 0 
for i in range(2023, N+1):
    num = str(i)
    if can_make_2023(num):
        count += 1
print(count)