movie_set = set()
i = 666

while len(movie_set) <= 10000:
    if "666" in str(i):
        movie_set.add(i)
    i += 1

movie_list = sorted(list(movie_set))

N = int(input())
print(movie_list[N-1])