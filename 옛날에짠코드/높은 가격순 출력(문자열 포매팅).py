Price = list(map(int, input().split(';')))
Price.sort(reverse=True)
for i in Price:
    print('%9s'% format(i, ','))