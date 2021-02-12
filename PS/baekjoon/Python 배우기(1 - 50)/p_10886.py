n = int(input())
cute = 0
not_cute = 0

for i in range(n):
    v = bool(int(input()))
    if v:
        cute += 1

    else:
        not_cute += 1

if cute > not_cute:
    print("Junhee is cute!")

else:
    print("Junhee is not cute!")