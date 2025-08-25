def dial_time(word):
    if word in ['A', 'B', 'C']:
        return 3
    elif word in ['D', 'E', 'F']:
        return 4
    elif word in ['G', 'H', 'I']:
        return 5
    elif word in ['J', 'K', 'L']:
        return 6
    elif word in ['M', 'N', 'O']:
        return 7
    elif word in ['P', 'Q', 'R', 'S']:
        return 8
    elif word in ['T', 'U', 'V']:
        return 9
    elif word in ['W', 'X', 'Y', 'Z']:
        return 10
    else:
        return 11

words = input()
time = 0
for word in words:
    time += dial_time(word)
print(time)