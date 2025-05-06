count = int(input())

for _ in range(count):
    sentence = input().rstrip()
    print(sentence if sentence.endswith('.') else f"{sentence}.")