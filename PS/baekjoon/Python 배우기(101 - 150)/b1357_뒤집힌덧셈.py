def rev(n):
    n = str(n)
    ans = ''
    for i in range(1, len(n)+1):
        ans += n[-i]

    return int(ans)


a, b = map(int, input().split())

print(rev(rev(a)+rev(b)))
