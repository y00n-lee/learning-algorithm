# 1 ≤ A, B ≤ 10,000
a, b = map(int, input().split())

while a<1 or b>10000:
    print("a가 1보다 작거나 b가 10000보다 큽니다")
    a, b = map(int, input().split())

print(a + b)
print(a - b)
print(a * b)
try:
    print(a // b)
    print(a % b)
except ZeroDivisionError:
    print("숫자를 0으로 나눌 수 없습니다.")
