N, M = map(int, input().split())
pokemon_dict = dict()
pokemon_dict_reverse = dict()

for i in range(1, N+1):
    pokemon = input()
    pokemon_dict[pokemon] = i
    pokemon_dict_reverse[i] = pokemon

for j in range(M):
    question = input()
    if question.isalpha():
        print(pokemon_dict[question])
    else:
        print(pokemon_dict_reverse[int(question)]) 