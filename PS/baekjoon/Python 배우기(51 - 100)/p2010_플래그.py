import sys

number = 0
n = int(input())
for _ in range(n):
    number += int(sys.stdin.readline())

print(number-n+1)