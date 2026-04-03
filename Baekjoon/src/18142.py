foods = input().split()
while "tapioka" in foods:
    if "tapioka" in foods:
        foods.remove("tapioka")

while "bubble" in foods:
    if "bubble" in foods:
        foods.remove("bubble")

if len(foods) != 0:
    for food in foods:
        print(food, end=" ")
else:
    print("nothing")