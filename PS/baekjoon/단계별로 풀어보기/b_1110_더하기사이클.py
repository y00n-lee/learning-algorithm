n = int(input())

a = n // 10
b = n % 10
count = 0

while(1):
    count += 1
    c = (a + b) % 10
    tmp = b * 10 + c

    if n == tmp:
        break

    else:
        a, b = b, c

print(count)
