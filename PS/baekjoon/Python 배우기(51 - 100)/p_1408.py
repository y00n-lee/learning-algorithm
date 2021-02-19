now_h, now_m, now_s = map(int, input().split(":"))
start_h, start_m, start_s = map(int, input().split(":"))

now = now_h * 3600 + now_m * 60 + now_s
start = start_h * 3600 + start_m * 60 + start_s

time = start - now if start >= now else 24 * 3600 - (now - start)

hour = time // 3600
time = time % 3600 if time >= 3600 else time
minute = time //60
time = time % 60 if time >= 60 else time
second = time

if hour < 10:
    print(f"0{hour}", end="")

else:
    print(f"{hour}", end="")

if minute < 10:
    print(f":0{minute}", end="")

else:
    print(f":{minute}", end="")

if second < 10:
    print(f":0{second}")

else:
    print(f":{second}")