n, amt = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

coins.reverse()
ans = 0
for i in range(n):
    if coins[i] <= amt:
        ans += amt // coins[i]
        amt %= coins[i]

    if amt == 0:
        break

print(ans)