n = int(input())
plans = list(map(str, input().split()))


move = ['L', 'R', 'U', 'D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]

x, y = 1, 1
for plan in plans:
    i = move.index(plan)
    nx = x + dx[i]
    ny = y + dy[i]
    # if x+dx[i]<= n and x+dx[i] >= 1 and y+dy[i] <=n and y+dy[i] >= 1:
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny

print(x, y)