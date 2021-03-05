for _ in range(int(input())):
    _ = int(input())
    store = list(map(int, input().split()))
    dist = max(store) - min(store)
    print(dist*2)

