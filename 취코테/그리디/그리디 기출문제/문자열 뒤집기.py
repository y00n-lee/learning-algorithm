data = input()

s = data[0]
f = data[-1]

count = 0

for i in range(1, len(data)):
    if data[i-1] != data[i]:
        count += 1

if s != f:
    print(count//2 + 1)

else:
    print(count//2)

