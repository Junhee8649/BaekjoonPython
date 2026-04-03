want = input()
ring_amount = int(input())
count = 0

for i in range(ring_amount):
    ring = input()
    plus_string = ring[0:len(want)]
    ring = ring + plus_string
    for j in range(10):
        if ring[j:j+len(want)] == want:
            count += 1
            break

print(count)