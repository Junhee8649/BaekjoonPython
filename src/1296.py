yeondu_name = input()
n = int(input())
max_prob = -1  
winner = ""

for _ in range(n):
    team_name = input()
    L = yeondu_name.count('L') + team_name.count('L')
    O = yeondu_name.count('O') + team_name.count('O')
    V = yeondu_name.count('V') + team_name.count('V')
    E = yeondu_name.count('E') + team_name.count('E')
    prob = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100

    if prob > max_prob:
        max_prob = prob
        winner = team_name
    elif prob == max_prob:
        if team_name < winner:
            winner = team_name

print(winner)