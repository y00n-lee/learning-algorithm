n = int(input())
ans = 0
for _ in range(n):
    word = input()
    checker = {word[0] : True}

    for i in range(1, len(word)):
        if word[i - 1] != word[i]:
            if checker.get(word[i]) is None:
                checker[word[i]] = True
            else:
                checker[word[i]] = False
                break

        elif word[i - 1] == word[i]:
            continue

    if list(checker.values()).count(False):
        pass
    else:
        ans += 1

print(ans)