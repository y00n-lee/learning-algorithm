# 피보나치 수 2

def Fibonacci(x):
    if x >= 2:
        for i in range(len(dp),x+1):
            dp.append(dp[i-1] + dp[i-2])
    return dp[x]

dp = [0,1]

print(Fibonacci(int(input())))
