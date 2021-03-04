score = {}
for i in range(1,6):
    s = list(map(int, input().split()))
    score[i] = sum(s)

max_score = max(score.values())
for k, v in score.items():
    if max_score == v:
        print(k,v)