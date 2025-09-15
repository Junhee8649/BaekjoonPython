garden = dict()
N = int(input())
for _ in range(N):
    animal = input()
    garden[animal] = garden.get(animal, 0) + 1
max_count_animal = max(garden, key=garden.get)
sum_animal = sum(garden.values())

if garden[max_count_animal] > sum_animal - garden[max_count_animal]:
   print(max_count_animal)
else:
    print("NONE")