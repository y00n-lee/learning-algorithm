chr_dict = {}
for i in range(26):
    chr_dict[chr(97+i)] = -1

word = input()
index = 0
for c in word:
    if chr_dict.get(c) == -1:
        chr_dict[c] = index
    index += 1

for v in chr_dict.values():
    print(v, end=" ")