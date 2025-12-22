birth = input()
N = int(input())
max_rhythm = 0
max_coding = "99991231"
for _ in range(N):
    coding = input()
    rhythm = ((int(birth[0]) - int(coding[0]))**2 + (int(birth[1]) - int(coding[1]))**2 + (int(birth[2]) - int(coding[2]))**2 + (int(birth[3]) - int(coding[3]))**2) * ((int(birth[4]) - int(coding[4]))**2 + (int(birth[5]) - int(coding[5]))**2) * ((int(birth[6]) - int(coding[6]))**2 + (int(birth[7]) - int(coding[7]))**2)
    if rhythm > max_rhythm:
        max_rhythm = rhythm
        max_coding = coding
    elif rhythm == max_rhythm:
        if int(max_coding) > int(coding):
            max_coding = coding
print(max_coding)