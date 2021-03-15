while(True):
    word = input()
    if word == "END":
        break

    for i in range(1, len(word)+1):
        print(word[-i], end="")
    print("")