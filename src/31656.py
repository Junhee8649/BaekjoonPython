S = input()
new_S = S[0]
for i in range(1,len(S)):
    if S[i] == S[i-1]:
        continue
    else:
        new_S += S[i] 
print(new_S)