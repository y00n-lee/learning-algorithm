n = int(input())

if n < 100:
    ans = n

else:
    ans = 99
    for i in range(100,n+1):
        i = str(i)
        d0 = int(i[0]) - int(i[1])
        check = True
        for j in range(2, len(i)):
            d = int(i[j-1])-int(i[j])
            if d0 != d:
                check = False
                break

        if check:
            ans += 1

print(ans)