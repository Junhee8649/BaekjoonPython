score = {
    0: 10,
    1: 8,
    2: 6,
    3: 5,
    4: 4,
    5: 3,
    6: 2,
    7: 1
}

races = []
for _ in range(8):
    races.append(input())
races.sort()

red = 0
blue = 0

for i in range(8):
    if races[i][-1] == "B":
        blue += score[i]
    else:
        red += score[i]

print("Red" if red > blue else "Blue")