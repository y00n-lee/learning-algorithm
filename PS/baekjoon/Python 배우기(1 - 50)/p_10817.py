li = [0]
li[0] = input().split()

for i in range(len(li[0])):
    li[0][i] = int(li[0][i])

li[0].sort()
print(li[0][1])