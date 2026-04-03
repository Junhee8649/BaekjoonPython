word = input()
count_JOI = 0
count_IOI = 0

for letter in range(len(word)-2):
    if word[letter:letter+3] == "JOI":
        count_JOI += 1
    elif word[letter:letter+3] == "IOI":
        count_IOI += 1

print(count_JOI)
print(count_IOI)