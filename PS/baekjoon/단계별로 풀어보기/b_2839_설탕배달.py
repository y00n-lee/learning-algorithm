data = int(input())
sugar = [3,5]

count = data // 3
answer = 0

for i in range(data//5 + 1):
    if i == 0 and data % 3 == 0:

        count = min(data // 3, count)

    elif (data % (5*i)) % 3 == 0:
        count = min(data // 5 + (data % 5) // 3, count)



print(count)