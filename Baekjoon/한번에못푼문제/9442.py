year = 0
while True:
    year += 1
    temp = input()
    if temp == "0":
        break
    n, s = temp.split()
    
    # 규칙 문자열로 우선순위 딕셔너리 생성
    order_dict = {char: i for i, char in enumerate(s)}

    words = []
    for i in range(int(n)):
        words.append(input())

    sorted_words = sorted(words, key=lambda word: [order_dict.get(char) for char in word])
    print(f"year {year}")
    for word in sorted_words:
        print(word)