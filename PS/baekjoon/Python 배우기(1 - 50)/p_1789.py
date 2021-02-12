
s = int(input())
sum = 0
count = 0
for i in range(1,s):
    sum += i
    count += 1
    if sum <= s < sum + i + 1:
        print(count)
        break