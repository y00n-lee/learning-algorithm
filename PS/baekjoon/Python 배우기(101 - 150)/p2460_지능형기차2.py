max = 0
total = 0
for _ in range(10):
    out_n, in_n = map(int, input().split())
    total += - out_n + in_n
    if total > max:
        max = total

print(max)