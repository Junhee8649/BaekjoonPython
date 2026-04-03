def password(S, testcase):
    is_in = False
    for i in testcase:
        if i in S: 
            is_in = True
            break
    return is_in
            

import string

N = int(input())
S = input()
count = 0

letters_lower = string.ascii_lowercase
letters_upper = string.ascii_uppercase
digits = string.digits
special_word = "!@#$%^&*()-+"

if password(S, letters_lower) == False:
    count += 1
if password(S, letters_upper) == False:
    count += 1
if password(S, digits) == False:
    count += 1
if password(S, special_word) == False:
    count += 1
print(max(count, 6 - N))