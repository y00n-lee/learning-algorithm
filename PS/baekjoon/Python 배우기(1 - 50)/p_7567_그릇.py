bowl = input()

height = 0
for i in range(len(bowl)):
    if i == 0:
        height += 10

    else:
        if bowl[i] == bowl[i-1]:
            height += 5

        else:
            height += 10

print(height)