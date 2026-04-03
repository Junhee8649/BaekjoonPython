import re

question = input()

for i in range(len(question)):
    if question[i] == '-':
        left = question[:i]
        right = question[i+1:]
        break
    else:
        left = question
        right = '0'

left_number = re.findall(r'\d+', left)
right_number = re.findall(r'\d+', right)
int_left_number = list(map(int, left_number))
int_right_number = list(map(int, right_number)) 

answer = sum(int_left_number) - sum(int_right_number)
print(answer)