A = 0 # 300 sec
B = 0 # 60 sec
C = 0 # 10 sec

t_second = int(input())

if t_second % 10 == 0:
    if t_second >= 300:
        A += t_second // 300
        t_second %= 300

    if t_second >= 60:
        B += t_second // 60
        t_second %= 60

    if t_second >= 10:
        C += t_second // 10

    print(A, B, C)


else:
    print(-1)

