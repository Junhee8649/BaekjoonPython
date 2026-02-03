N = int(input())
sentence = "baby sukhwan tururu turu very cute tururu turu in bed tururu turu baby sukhwan".split()
ddurru = [3,4,7,8,11,12]
num = (N - 1) % 14
word = sentence[num]
if N % 14 in ddurru:
    plus_ru = N // 14
    word += "ru" * plus_ru
    if word.count("ru") >= 5:
        word = "tu+ru*" + str(word.count("ru"))
print(word)