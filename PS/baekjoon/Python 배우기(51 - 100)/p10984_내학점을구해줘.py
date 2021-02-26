for _ in range(int(input())):
    total = 0
    gpa = 0.0
    for _ in range(int(input())):
        t, a = map(float, input().split())
        total += t
        gpa += t * a

    print(int(total), round(gpa/total, 1))