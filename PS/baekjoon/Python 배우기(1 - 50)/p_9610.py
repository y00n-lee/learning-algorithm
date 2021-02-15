#  사분면

n = int(input())

axis = 0
q = [0, 0, 0, 0]

for i in range(n):
    x, y = map(int, input().split())

    if x > 0 and y > 0:
        q[0] += 1

    elif x < 0 and y > 0:
        q[1] += 1

    elif x < 0 and y < 0:
        q[2] += 1

    elif x > 0 and y < 0:
        q[3] += 1

    else:
        axis += 1

for i in range(len(q)):
    print(f"Q{i + 1}: {q[i]}")

print(f"AXIS: {axis}")
