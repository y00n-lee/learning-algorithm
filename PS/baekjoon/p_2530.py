hour, minute, second = map(int, input().split())
time = int(input())

hour += time//3600
time %= 3600
minute += time//60
second += time%60

if second >= 60:
    minute += second//60
    second %= 60

if minute >= 60:
    hour += minute//60
    minute %= 60

if hour >= 24:
    hour %= 24

print(hour, minute, second)