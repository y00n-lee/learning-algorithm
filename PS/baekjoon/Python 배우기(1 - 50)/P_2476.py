n = int(input())
num = []

for i in range(n):
    a, b, c = map(int, input().split())
    num.append([a, b, c])

reward = []
for i in range(n):
    t1 = True if num[i][0] == num[i][1] else False
    t2 = True if num[i][1] == num[i][2] else False
    t3 = True if num[i][0] == num[i][2] else False
    max_n = max(num[i])

    if t1 and t2 and t3:
        reward.append(10000 + max_n * 1000)
    elif not t1 and not t2 and not t3:
        reward.append(max_n * 100)
    else:
        if t1:
            max_n = num[i][0]
        elif t2:
            max_n = num[i][1]
        else:
            max_n = num[i][2]

        reward.append(1000 + max_n * 100)

print(max(reward))
