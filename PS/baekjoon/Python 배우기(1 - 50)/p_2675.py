T = int(input())
li = []
for i in range(T):
    li.append(input().split())

for i in range(T):
    ans = ""
    for letter in li[i][1]:
        for num in range(int(li[i][0])):
            ans += letter

    print(ans)