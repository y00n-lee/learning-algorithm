sentence = input()

ans = ""
for c in sentence:
    asci = ord(c)

    if 65 <= asci <= 90:
        if asci >= 78:
            ans += chr(asci - 13)

        else:
            ans += chr(asci + 13)

    elif 97 <= asci <= 122:
        if asci >= 110:
            ans += chr(asci - 13)

        else:
            ans += chr(asci + 13)

    else:
        ans += c

print(ans)