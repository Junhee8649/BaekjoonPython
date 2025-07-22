from itertools import combinations

small_man = 9
small_man_list = []
for _ in range(small_man):
    small_man_list.append(int(input()))

for com in combinations(small_man_list, 7):
    if sum(com) == 100:
        answer = list(com)
        answer.sort()
        for people in answer:
            print(people)
        break