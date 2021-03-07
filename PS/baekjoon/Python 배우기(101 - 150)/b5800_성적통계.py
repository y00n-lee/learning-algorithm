for i in range(int(input())):
    print(f"Class {i+1}")
    tmp = list(map(int, input().split()))
    del tmp[0]
    tmp.sort(reverse=True)
    gap = 0
    for index in range(1,len(tmp)):
        g = abs(tmp[index-1] - tmp[index])
        if gap < g:
            gap = g

    print(f"Max {max(tmp)}, Min {min(tmp)}, Largest gap {gap}")