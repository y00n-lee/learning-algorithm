data = int(input())
sugar = [(data//3)+1, (data//5)+1]

count = sugar[0] + sugar[1]
flag = True

for i in range(sugar[0]):
    for j in range(sugar[1],-1,-1):
        if 3*i + 5*j == data:
            count = min(i+j,count)
            flag = False

        else:
            continue

if flag:
    print(-1)

else:
    print(count)

