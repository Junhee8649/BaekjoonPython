W, K = [], []
for _ in range(10):
  W.append(int(input()))
W.sort(reverse=True)
for _ in range(10):
  K.append(int(input()))
K.sort(reverse=True)
W_sum = sum(W[0:3])
K_sum = sum(K[0:3])
print(W_sum, K_sum)