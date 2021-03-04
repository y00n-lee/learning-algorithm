a, b = map(int, input().split())
ans = 0
for n in range(a, b+1):

    for i in range(46):    # 45 * 46 /2 = 1035  이므로 a,b의 범위를 만족
        min_bound = i*(i-1)//2
        max_bound = i*(i+1)//2
        if min_bound < n <= max_bound:
            ans += i


print(ans)


