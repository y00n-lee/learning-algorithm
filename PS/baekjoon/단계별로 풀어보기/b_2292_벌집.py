n = int(input())

tmp = 1
ans = 1
while n > tmp:
    tmp = tmp + (6 * ans)
    ans += 1

print(ans)