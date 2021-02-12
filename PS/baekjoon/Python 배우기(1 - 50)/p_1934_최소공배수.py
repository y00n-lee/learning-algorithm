t = int(input())

def GCD(a, b):
    x = 0
    y = 0

    if a > b:
        x = a
        y = b

    elif a < b:
        x = b
        y = a

    else:
        return a

    while x%y != 0:
        tmp = x % y
        x = y
        y = tmp

    return y

def LCM(a, b):
    gcd = GCD(a, b)
    return int(a * b / gcd)

for i in range(t):
    a, b = map(int, input().split())

    print(LCM(a,b))

