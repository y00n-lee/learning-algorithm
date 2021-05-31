t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    y = h if n % h == 0 else n % h
    x = n // h if n % h == 0 else n // h + 1

    if x < 10:
        print(f"{y}0{x}")

    else:
        print(f"{y}{x}")
