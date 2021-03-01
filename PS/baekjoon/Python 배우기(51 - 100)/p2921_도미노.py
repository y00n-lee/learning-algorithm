n = int(input())
num = 0
for i in range(1, n+2):  #1부터 N+1까지
    num += (2*i -1)

print(((num - n - 1)//2 + n + 1)*n) #{(num - (n+1))/2 + (n+1)} * n, n+1인 이유는 점의 개수가 0부터 n이 될 수 있으므로