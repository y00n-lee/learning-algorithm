from datetime import datetime

year = datetime.today().year
month = datetime.today().month
day = datetime.today().day
if month<10:
    print(f"{year}-0{month}-0{day}") if day<10 else print(f"{year}-0{month}-{day}")
else:
    print(f"{year}-{month}-0{day}") if day<10 else print(f"{year}-{month}-{day}")

