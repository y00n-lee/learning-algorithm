for _ in range(3):
    state = list(map(int,input().split()))
    if sum(state) == 3:
        print("A")

    elif sum(state) == 2:
        print("B")

    elif sum(state) == 1:
        print("C")

    elif sum(state) == 0:
        print("D")

    elif sum(state) == 4:
        print("E")