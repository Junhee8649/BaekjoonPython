def decison(cm, kg):
    bmi = kg / (cm/100)**2
    if cm < 140.1: return 6
    elif 140.1 <= cm < 146: return 5
    elif (146 <= cm < 159) or (159 <= cm < 161 and (bmi < 16 or bmi >= 35)) or (161 <= cm < 204 and (bmi < 16 or bmi >= 35)) or cm >= 204: return 4
    elif (159 <= cm < 161 and 16 <= bmi < 35) or (161 <= cm < 204 and (16 <= bmi < 18.5 or 30 <= bmi < 35)): return 3
    elif (161 <= cm < 204) and (18.5 <= bmi < 20 or 25 <= bmi < 30): return 2
    elif 161 <= cm < 204 and 20 <= bmi < 25: return 1

t = int(input())
for i in range(t):
    cm, kg = map(int, input().split())
    print(decison(cm, kg))
