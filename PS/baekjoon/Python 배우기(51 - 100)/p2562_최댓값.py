ans = [0]
max = -1
for _ in range(9):
    num = int(input())
    ans.append(num)
    if num > max:
        max = num

print(max)
print(ans.index(max))

