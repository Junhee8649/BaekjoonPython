T = int(input())
for _ in range(T):
    S = input()
    X_not = ""
    for i in range(len(S)-1):
        if S[i:len(S)-1] != S[-1:i:-1]:
            X_not += S[i]
        else:
            break
    S += X_not[-1::-1]
    print(S)