import sys


n = int(sys.stdin.readline())
people = set()
for i in range(n):
    name, status = sys.stdin.readline().split()
    if status == "enter":
        people.add(name)
    else:
        people.remove(name)
people = list(people)
people.sort(reverse=True)
for person in people:
    print(person)