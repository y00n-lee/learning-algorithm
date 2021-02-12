t = int(input())

for i in range(t):
    r, e, c = map(int, input().split())
    if e > r + c:
        print("advertise")

    elif e < r + c:
        print("do not advertise")

    elif e == r + c:
        print("does not matter")