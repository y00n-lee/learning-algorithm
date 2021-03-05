score = {}
for number in range(8):
    n = int(input())
    score[n] = number+1

tmp = sorted(score.keys(), reverse=True)
print(sum(tmp[:5]))

del score[tmp[5]], score[tmp[6]], score[tmp[7]]

for n in sorted(score.values()):
    print(n, end=" ")
