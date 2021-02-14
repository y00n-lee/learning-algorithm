chang = 100
sang = 100

round = int(input())

for i in range(round):
    c, s = map(int, input().split())
    if c > s:
        sang -= c

    elif c < s:
        chang -= s

print(chang)
print(sang)