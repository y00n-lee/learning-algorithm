for _ in range(int(input())):
    num = list(map(int, input().split()))
    eval_num = []

    for i in num:
        if i % 2 == 0:
            eval_num.append(i)
    print(sum(eval_num), min(eval_num))
