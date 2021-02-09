T = int(input())
mars = []

for i in range(T):
    mars.append(input().split())

# for i in range(len(mars)):
for row in mars:
    ans = 0
    for index in range(len(row)):
        if index == 0:
            ans += float(row[index])
        else:
            if row[index] == "@":
                ans *= 3
            elif row[index] == "%":
                ans += 5
            elif row[index] == "#":
                ans -= 7
    print("%.2f" %ans)
