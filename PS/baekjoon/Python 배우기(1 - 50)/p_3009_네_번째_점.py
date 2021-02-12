s = []

for i in range(3):
    a, b = map(int, input().split())
    s.append([a, b])

point = []
for i in range(2):
    if s[1][i] == s[2][i]:
        point.append(s[0][i])

    elif s[0][i] == s[2][i]:
        point.append(s[1][i])

    else:
        point.append(s[2][i])

print(point[0], point[1])