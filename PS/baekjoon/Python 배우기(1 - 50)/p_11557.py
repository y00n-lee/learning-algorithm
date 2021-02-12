t = int(input())

for i in range(t):
    n = int(input())

    dict = {}
    for j in range(n):
        school, liter = input().split()
        dict[int(liter)] = school

    ans = max(dict.keys())
    print(dict.get(ans))