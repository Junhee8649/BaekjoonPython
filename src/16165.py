N, M = map(int, input().split())
all_member = []
all_team = []
for _ in range(N):
    all_team.append(input())
    member_count = int(input())
    each_team_member = []
    for _ in range(member_count):
        each_team_member.append(input())
    each_team_member.sort()
    all_member.append(each_team_member)

for _ in range(M):
    member_or_team = input()
    quiz = int(input())
    if quiz == 0:
        for i in range(len(all_team)):
            if member_or_team == all_team[i]:
                for mem in all_member[i]:
                    print(mem)
                break
    else:
        for j in range(len(all_member)):
            if member_or_team in all_member[j]:
                print(all_team[j])
                break
