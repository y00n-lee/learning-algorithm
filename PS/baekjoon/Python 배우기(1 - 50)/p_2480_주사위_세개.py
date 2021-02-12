a, b, c = map(int, input().split())
if a == b and b == c and c == a:
    print(10000 + a * 1000)

elif a != b and b != c and c != a:
    max_n = max(a, b, c)
    print(max_n * 100)

else:
    same_n = a if a == b or a == c else b
    print(1000 + same_n * 100)
