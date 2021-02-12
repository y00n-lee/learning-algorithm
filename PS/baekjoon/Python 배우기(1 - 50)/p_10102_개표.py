judge_num = int(input())
vote = input()
count_a = 0
count_b = 0
for i in range(judge_num):
    if vote[i] == "A":
        count_a += 1

    elif vote[i] == "B":
        count_b += 1

if count_a > count_b:
    print("A")

elif count_a < count_b:
    print("B")

else:
    print("Tie")