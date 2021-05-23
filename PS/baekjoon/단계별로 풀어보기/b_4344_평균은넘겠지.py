for _ in range(int(input())):
    score = list(map(int,input().split()))
    sum = 0
    for s in score[1:]:
        sum += s
    avg = float(sum/score[0])
    avg_over = 0
    for s in score[1:]:
        if s > avg:
            avg_over += 1

    print(f"{avg_over/score[0]*100:.3f}%")