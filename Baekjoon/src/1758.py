N = int(input())
people = []
for _ in range(N):
    people.append(int(input()))
people.sort(reverse=True)
minus_money = 0
final_money = 0
for person in people:
    tip = (person - minus_money)
    if tip > 0:
        final_money += tip
    minus_money += 1
print(final_money)