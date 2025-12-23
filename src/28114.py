team = []
for i in range(3):
    team.append(input().split())
for i in range(3):
    team[i][0] = int(team[i][0])
    team[i][1] = int(team[i][1])%100
team.sort(key=lambda x: x[1])
first_team_name = str(team[0][1]) + str(team[1][1]) + str(team[2][1]) 
print(first_team_name)
team.sort(reverse = True, key=lambda x: x[0])
second_team_name = team[0][2][0] + team[1][2][0] + team[2][2][0] 
print(second_team_name)