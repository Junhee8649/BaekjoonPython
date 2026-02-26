def jjanken(a, b):
  one, two = 0, 0
  if (a == 'R' and b == 'S') or (a == 'S' and b == 'P') or (a == 'P' and b == 'R'):
    one += 1
  elif a == b:
    pass
  else:
    two += 1
  return one, two
  

t = int(input())
for i in range(t):
  n = int(input())
  player_one, player_two = 0, 0
  for j in range(n):
    a, b = input().split()
    one, two = jjanken(a,b)
    player_one += one
    player_two += two
  if player_one > player_two:
    print("Player 1")
  elif player_one == player_two:
    print("TIE")
  else:
    print("Player 2")