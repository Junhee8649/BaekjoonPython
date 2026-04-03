from itertools import permutations
import sys


T = int(input())
for i in range(T):
    word = sys.stdin.readline().strip()
    word_comb = permutations(word, len(word))
    print(f"Case # {i+1}:")
    for comb in word_comb:
        print("".join(comb))