for i in range(int(input())):
    seat = {}
    p, m = map(int, input().split())
    count = 0
    for i in range(m):
        seat[i+1] = 0
    for i in range(p):
        num = int(input())
        if num in seat.keys():
            if seat.get(num) == 0:
                seat[num] += 1

            else:
                count += 1
    print(count)

