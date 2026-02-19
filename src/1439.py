def target(num, S):
  i = 0
  count = 0
  already = False
  while i < len(S):
    if S[i] == num:
      if not already:
        count += 1
        already = True
    else:
      already = False
    i += 1
  return count
  
S = input()
a = target('0', S)
b = target('1', S)
print(min(a, b))