n = int(input())

for i in range(1, n):
    print("*" * i,end="")
    print(" " * 2*(n-i),end="")
    print("*" * i)

for i in range(n, 0, -1):
    print("*" * i,end="")
    print(" " * 2*(n-i),end="")
    print("*" * i)