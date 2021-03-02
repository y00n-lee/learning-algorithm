def solve():
    min_n = int(input())
    max_n = int(input())
    ans = []
    for num in range(min_n,max_n+1):
        flag = True
        sqrt = int(num**0.5)
        for i in range(2,sqrt + 1):
            if num % i == 0:
                flag = False
                break

        if flag and num >= 2:
            ans.append(num)

    if len(ans):
        print(sum(ans))
        print(min(ans))
    else:
        print(-1)

solve()
