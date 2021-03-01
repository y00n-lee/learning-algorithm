_, x = map(int, input().split())
num_list = map(int, input().split())
ans = []
for i in num_list:
    if i < x:
       print(i, end=" ")

