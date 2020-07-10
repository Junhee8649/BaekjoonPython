table = str.maketrans(',.', '  ')
k = input().translate(table).split()
ct = 0
for i in k:
    if i == 'the':
        ct += 1
print(ct)