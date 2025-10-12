def is_word(words):
    if len(words) % 2 != 0:
        return -999
    answer = ""
    while len(words) > 0:
        if (len(words) - 4) >= 0:
            answer += "AAAA"
            words = words[4:]
        elif (len(words) - 2) >= 0:
            answer += "BB"
            words = words[2:]
        else:
            break
    return answer

board = input()
temp = 0
real_answer = ""
is_can = True
for i in range(len(board)):
    if board[i] == '.':
        if board[i-1] == '.' or i == 0:
            real_answer += "."
            temp = i+1
            continue
        if is_word(board[temp:i]) == -999:
            print(-1)
            is_can = False
            break
        else:
            real_answer += is_word(board[temp:i])
            real_answer += "."
            temp = i+1
if is_can:
    if is_word(board[temp:]) == -999:
        print(-1)
    else:
        print(real_answer, end="")
        print(is_word(board[temp:]))