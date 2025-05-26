word1 = input()
word2 = input()
word3 = input()
word4 = input()
word5 = input()

max_length = max(len(word1), len(word2),len(word3),len(word4),len(word5))
word1 = word1 + " " * (max_length - len(word1))
word2 = word2 + " " * (max_length - len(word2))
word3 = word3 + " " * (max_length - len(word3))
word4 = word4 + " " * (max_length - len(word4))
word5 = word5 + " " * (max_length - len(word5))

for i in range(max_length):
    print(f"{word1[i]}{word2[i]}{word3[i]}{word4[i]}{word5[i]}".replace(" ", "" ), end="")