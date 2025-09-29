def I(R, G, B):
    Intensity = 2126*R + 7152*G + 722*B
    if Intensity < 510000:
        return "#"
    elif Intensity < 1020000:
        return "o"
    elif Intensity < 1530000:
        return "+"
    elif Intensity < 2040000:
        return "-"
    else:
        return "."
    
N, M = map(int, input().split())
for i in range(N):
    color_line = list(map(int, input().split()))
    for j in range(0, 3*M, 3):
        print(I(color_line[j], color_line[j+1], color_line[j+2]), end="")
    print()