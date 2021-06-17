n, k = map(int, input().split())
result = 0

while n != 1:
    if n % k == 0:
        n //= k
        result += 1

    elif n < k:
        result += n - 1
        n -= n - 1


    else:
        result += n % k
        n -= n % k

print(result)