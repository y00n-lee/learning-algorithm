m = int(input())
n = int(input())

perfect_square = []

min_n = int(m**0.5)
max_n = int(n**0.5)

for i in range(min_n,max_n + 1):
    if m <= i**2 <= n:
        perfect_square.append(int(i**2))
if len(perfect_square):
    print(sum(perfect_square))
    print(min(perfect_square))

else:
    print(-1)
