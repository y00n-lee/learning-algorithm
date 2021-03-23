word = input()
index = 0
for c in word:
    print(c,end ="")
    index += 1

    if index % 10 == 0:
        print("")