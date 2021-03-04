sum = 0
mode = {}

for _ in range(10):
    n = int(input())
    sum += n

    if n in mode:
        mode[n] += 1

    else:
        mode[n] = 1

print(sum//10)
mode_max = max(mode.values())
for k,v in mode.items():
    if v == mode_max:
        print(k)
        break