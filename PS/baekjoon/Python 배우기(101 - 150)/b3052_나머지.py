mod = {}

for _ in range(10):
    n = int(input())
    if n%42 in mod:
        mod[n%42] += 1

    else:
        mod[n%42] = 1

print(len(mod))