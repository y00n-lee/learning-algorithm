test_case = int(input())

for i in range(test_case):
    player_number = int(input())
    high_money = 0
    player_name = ""
    for j in range(player_number):
        money, name = input().split()
        money = int(money)
        if high_money < money:
            high_money = money
            player_name = name

    print(player_name)
