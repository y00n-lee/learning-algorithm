T = int(input())
a = []
b = []
for i in range(T):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

for i in range(T):
    print(f"Case #{i+1}: {a[i]} + {b[i]} = {a[i]+b[i]}")