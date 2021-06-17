state = input()

x, y = ord(state[0]) - ord('a') + 1, int(state[1])

steps = [(2,-1),(2,1),(-2,-1),(-2,1),
         (-1,-2),(1,-2),(-1,2),(1,2)]

count = 0
for (dx, dy) in steps:
    nx = x + dx
    ny = y + dy
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)
