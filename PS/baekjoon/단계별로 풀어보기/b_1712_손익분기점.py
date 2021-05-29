a, b, c = map(int, input().split())
try:
    ans = a / (c - b)
except ZeroDivisionError:
    ans = -1

if ans < 0:
    ans = -1

else:
    ans = int(ans) + 1

print(ans)