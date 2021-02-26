count = 0
for _ in range(int(input())):
    stu, apple = map(int, input().split())
    count += apple % stu

print(count)