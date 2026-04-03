keyboard = []
for _ in range(4):
    keyboard.append(input())
find_word = input()

for i in range(2):
    for j in range(8):
        is_answer = True
        temp_word = keyboard[i][j:j+3] + keyboard[i+1][j:j+3] + keyboard[i+2][j:j+3]
        for letter in temp_word:
            if letter not in find_word:
                is_answer = False
                break
        if is_answer:
            print(keyboard[i+1][j+1])
            break