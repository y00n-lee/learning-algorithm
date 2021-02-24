stu_number = int(input())

older = ""
younger = ""

younger_birth = -1
older_birth = -1

for i in range(stu_number):
    name, day, month, year = input().split()
    day, month, year = map(int, [day, month, year])

    if younger_birth == -1 and older_birth == -1:
        older = name
        younger = name
        younger_birth = [year, month, day]
        older_birth = [year, month, day]

    else:
        if year < older_birth[0]:
            older = name
            older_birth = [year, month, day]

        elif year == older_birth[0] and month < older_birth[1]:
            older = name
            older_birth = [year, month, day]

        elif year == older_birth[0] and month == older_birth[1] and day < older_birth[2]:
            older = name
            older_birth = [year, month, day]

        if year > younger_birth[0]:
            younger = name
            younger_birth = [year, month, day]

        elif year == younger_birth[0] and month > younger_birth[1]:
            younger = name
            younger_birth = [year, month, day]

        elif year == younger_birth[0] and month == younger_birth[1] and day > younger_birth[2]:
            younger = name
            younger_birth = [year, month, day]

        else:
            pass

print(younger)
print(older)
