def divisor_number(n):
    divisor = []
    divisor_back = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor.append(i)

            if i != (n // i):
                divisor_back.append(n // i)

    return divisor + divisor_back[::-1]


while True:
    n = int(input())
    if n == -1:
        break

    d = divisor_number(n)
    d.pop()

    if sum(d) == n:
        print(f"{n} = {d[0]}", end="")
        for index in range(1, len(d)):
            print(f" + {d[index]}", end="")
        print("")

    else:
        print(f"{n} is NOT perfect.")
