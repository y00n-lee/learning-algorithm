number = list(map(int, input().split()))

ans = 0
for n in number:
    ans += n**2

print(ans%10)