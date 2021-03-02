day = int(input())
car_num = list(map(int, input().split()))
ans = 0
for num in car_num:
    if num == day:
        ans += 1

print(ans)