n, k = map(int, input().split())
div = [0]
sqrt = int(n ** 0.5)
for i in range(1, sqrt + 1):
    if n % i == 0:
        div.append(i)
        if i != (n // i):
            div.append(n // i)

div.sort()
try:
    print(div[k])
except:
    print(0)
