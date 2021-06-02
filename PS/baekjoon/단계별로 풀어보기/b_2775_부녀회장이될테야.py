t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    neighbor = [[]]
    for i in range(n):
        neighbor[0].append(i+1)

    for i in range(k):
        tmp_arr = []
        for j in range(n):
            tmp = 0
            for m in range(j+1):
                tmp += neighbor[i][-(n)+m]

            tmp_arr.append(tmp)
        neighbor.append(tmp_arr)

    print(neighbor[k][n-1])

