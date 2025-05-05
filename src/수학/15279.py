n = int(input())
for i in range(n):
    b, p = map(float, input().split())
    bpm = 60 * b / p
    min_bpm = 60 * (b-1) / p
    max_bpm = 60 * (b+1) / p
    print(f"{min_bpm} {bpm} {max_bpm}")