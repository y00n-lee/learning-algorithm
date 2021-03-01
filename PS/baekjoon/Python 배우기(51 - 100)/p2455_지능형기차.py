people = []
for i in range(4):
    a, b = map(int, input().split())
    if i == 0:
        people.append(b)
    else:
        people.append(people[i-1]-a+b)

print(max(people))