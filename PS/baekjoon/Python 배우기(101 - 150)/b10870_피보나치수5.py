fib = [0, 1]
n = int(input())

if n < 2:
    print(fib[n])

else:
    for _ in range(n-1):
        num = fib[-1] + fib[-2]
        fib.append(num)

    print(fib[-1])
