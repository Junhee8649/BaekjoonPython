N = int(input())
count = 0
clap = ["3","6","9"]
for num in range(N+1):
    target = str(num)
    count += target.count("3") + target.count("6") + target.count("9")
print(count) 