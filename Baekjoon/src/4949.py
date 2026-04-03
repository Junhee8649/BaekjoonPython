from collections import deque

sentence = input()

while(sentence != '.'):
    stack = deque()
    answer = True
    for i in sentence:
        if i == '(':
            stack.append('(')
        elif i == '[':
            stack.append('[')
        elif i == ')':
            if len(stack) == 0:
                answer = False
                break
            if stack[-1] != '(':
                answer = False
            else:
                stack.pop()
        elif i == ']':
            if len(stack) == 0:
                answer = False
                break
            if stack[-1] != '[':
                answer = False
            else:
                stack.pop()
    if len(stack) != 0:
        answer = False
  
    print("yes" if answer == True else "no")

    sentence = input()