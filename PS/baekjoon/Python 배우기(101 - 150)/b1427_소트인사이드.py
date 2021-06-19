data = input()
number = []
for n in data:
    number.append(int(n))

number.sort(reverse=True)

for i in number:
    print(i, end="")