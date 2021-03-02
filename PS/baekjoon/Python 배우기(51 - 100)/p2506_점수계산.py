p_num = int(input())
ox_score = list(map(int, input().split()))
ans = []
flag = False
for i in range(len(ox_score)):
    if ox_score[i] == 0:
        flag = False

    if flag:
        ans.append(ans[-1]+1)
        continue

    if ox_score[i]:
        ans.append(1)
        flag = True

print(sum(ans))