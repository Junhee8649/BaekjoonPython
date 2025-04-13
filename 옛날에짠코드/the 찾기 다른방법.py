k = input().split()
ct = 0
for i in k:
    if i.strip(',.') == 'the':
        ct += 1
print(ct)