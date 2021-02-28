n = int(input())

for i in range(1, 2*n + 1):
    if i <= n:
        print(" " * (n - i), end="")
        print("*" * (2 * i - 1))

    else:
        print(" " * (i - n), end ="")
        print("*" * (4 * n - 2 * i -1))
