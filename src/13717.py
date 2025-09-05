def evolution(K, M):
    evolution_candy = 0
    while M // K > 0:
        M = M - K + 2
        evolution_candy += 1
    return evolution_candy

N = int(input())
count, max_candy = 0, 0
pokemon_and_candy = []
for _ in range(N):
    pokemon = input()
    candy_K, candy_M = map(int, input().split())
    final_candy = evolution(candy_K, candy_M)

    count += final_candy
    pokemon_and_candy.append([pokemon, final_candy])
    if final_candy > max_candy:
        max_candy = final_candy

print(count)
for i in range(N):
    if pokemon_and_candy[i][1] == max_candy:
        print(pokemon_and_candy[i][0])
        break