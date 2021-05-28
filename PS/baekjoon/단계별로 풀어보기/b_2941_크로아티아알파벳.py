croatia = {"c=": 0, "c-": 0, "dz=": 0, "d-": 0, "lj": 0, "nj": 0, "s=": 0, "z=": 0}

word = input()
ans = len(word)

for key in croatia.keys():
    if word.count(key) and key != "z=":
        croatia[key] += word.count(key)

    if key == "z=":

        croatia[key] = word.count(key) - word.count("dz=")


for key, value in croatia.items():
    if key != "dz=":
        ans -= value

    else:
        ans -= 2 * value
        
print(ans)