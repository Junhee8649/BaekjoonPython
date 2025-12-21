import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    people = []
    count = 1
    for _ in range(N):
        people.append(list(map(int, input().split())))

    people.sort()
    min_interview_rank = people[0][1]
    for i in range(1,N):
        current_interview_rank = people[i][1]
        if current_interview_rank < min_interview_rank:
            count += 1 
            min_interview_rank = current_interview_rank 
    print(count)