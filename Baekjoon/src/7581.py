def cuboid(i, w, h, v):
    if i == 0:
        i = int(v / (w * h))
    elif w == 0:
        w = int(v / (i * h))
    elif h == 0:
        h = int(v / (i * w))
    elif v == 0:
        v = int(i * w * h)
    print(i, w, h, v)

i, w, h, v = map(int, input().split())

while i!= 0 or w != 0 or h != 0 or v != 0:
    cuboid(i, w, h, v)
    i, w, h, v = map(int, input().split())