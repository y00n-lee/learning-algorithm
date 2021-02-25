# 피보나치 수 - 백준 2747번

#DP 사용 방법
dp =[0,1]
for i in range(2, 46):
    dp.append(dp[i-1] + dp[i-2])

print(dp[int(input())])


# #재귀함수 사용 방법 - 시간 초과
# def Fibonacci(x):
#     if x == 0:
#         return 0
#
#     if x == 1:
#         return 1
#
#     if x >= 2 :
#         return Fibonacci(x-1) + Fibonacci(x-2)
#
# n = int(input())
# print(Fibonacci(n))