for _ in range(int(input())):
    ans = ""
    pos, word = input().split()
    pos = int(pos)
    for index in range(len(word)):
        if index == pos - 1:
            continue
        ans += word[index]
    print(ans)
