import math
a, b, v = map(int, input().split())

ans = math.ceil((v - a)/(a - b)) + 1
print(ans)