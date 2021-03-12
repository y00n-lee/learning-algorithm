word = input()
word = word.upper()

letter = {}

for c in word:
    if c not in letter:
        letter[c] = 1

    else:
        letter[c] += 1

num_max = max(letter.values())
ans = ''
for k,v in letter.items():
    if v == num_max and ans == '':
        ans = k
    elif v == num_max and ans != '':
        ans = '?'

print(ans)



