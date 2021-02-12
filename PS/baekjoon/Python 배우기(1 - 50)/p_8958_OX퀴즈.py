def calc_score(s=[]):
    sum = 0
    for i in s:
        if len(i) != 0:
            score = len(i)
            sum += int(score * (score + 1)/2)
    print(sum)


test_case = int(input())

for i in range(test_case):
    calc_score(input().split("X"))


