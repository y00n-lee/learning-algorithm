height = []
for _ in range(9):
    height.append(int(input()))

value = sum(height) - 100
for i in range(len(height)-1):
    one = height[i]
    flag = False
    for j in range(i+1, len(height)):
        two = height[j]

        if (one + two) == value:
            height.remove(one)
            height.remove(two)
            flag = True
            break

    if flag:
        break
height.sort()
for v in height:
    print(v)
