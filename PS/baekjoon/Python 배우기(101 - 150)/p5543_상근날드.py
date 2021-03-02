min_burger = 0
min_drink = 0

for i in range(3):
    burger_price = int(input())
    if i == 0:
        min_burger = burger_price

    if min_burger > burger_price:
        min_burger = burger_price


for j in range(2):
    drink_price = int(input())
    if j == 0:
        min_drink = drink_price

    if min_drink > drink_price:
        min_drink = drink_price

print(min_burger + min_drink - 50)