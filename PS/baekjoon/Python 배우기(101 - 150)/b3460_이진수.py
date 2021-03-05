for i in range(int(input())):
    num = int(input())
    i = 0
    while num:
        if num % 2:
            print(i,end = " ")
        i += 1
        num //= 2
    print("")