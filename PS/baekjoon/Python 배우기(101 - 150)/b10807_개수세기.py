t = int(input())

nums = list(map(int, input().split()))
val = int(input())

ans = 0
for i in nums:
    if i == val:
        ans += 1

print(ans)