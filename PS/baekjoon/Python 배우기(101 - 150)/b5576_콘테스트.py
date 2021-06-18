score = []
for _ in range(20):
    score.append(int(input()))

w_score = score[:10]
s_score = score[10:]

w_score.sort(reverse=True)
s_score.sort(reverse=True)

print(sum(w_score[:3]), sum(s_score[:3]))