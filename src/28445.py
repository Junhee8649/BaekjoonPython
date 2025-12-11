dad = input().split()
mom = input().split()
colors = list({*dad, *mom})
colors.sort()
for i in range(len(colors)):
    for j in range(len(colors)):
        print(colors[i], colors[j])