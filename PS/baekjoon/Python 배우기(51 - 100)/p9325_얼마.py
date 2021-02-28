for _ in range(int(input())):
    total = 0
    total += int(input())
    for _ in range(int(input())):
        q, p = map(int, input().split())
        total += q * p
    print(total)