croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()
count = 0
letter = 0

while letter < len(word)-2:
    if word[letter:letter+2] in croatia:
        count += 1
        letter += 2
    elif word[letter:letter+3] in croatia:
        count += 1
        letter += 3
    else:
        count += 1
        letter += 1
if letter == len(word)-2:
    if word[letter:letter+2] in croatia:
        count += 1
    else:
        count += 2
elif letter == len(word)-1:
    count += 1
    
print(count)