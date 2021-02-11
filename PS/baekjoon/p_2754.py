score = input()
ans = 0.0
for s in score:
    if s == "A":
        ans += 4.0

    elif s == "B":
        ans += 3.0

    elif s == "C":
        ans += 2.0

    elif s == "D":
        ans += 1.0

    else:
        if s == "+":
            ans += 0.3
        elif s == "-":
            ans -= 0.3

print(ans)