for _ in range(int(input())):
    score = list(map(int, input().split()))
    score.sort()
    if score[3]-score[1] >= 4:
        print("KIN")
        continue
    print(sum(score[1:4]))