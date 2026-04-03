A = input()
B = input()
answer = input()
is_answer_A = False
is_answer_B = False

for i in range(len(A)-len(answer)+1):
    if A[i:i+len(answer)] == answer:
        is_answer_A = True
for j in range(len(B)-len(answer)+1):
    if B[j:j+len(answer)] == answer:
        is_answer_B = True

if is_answer_A and is_answer_B:
    print("YES")
else:
    print("NO")