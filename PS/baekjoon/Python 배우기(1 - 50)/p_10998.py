a, b = map(int, input().split())
while(a<=0 or b>=10):
    print("a가 0보다 작거나 같고 b가 10보다 크거나 같습니다.")
    a, b = map(int, input().split())
print(a*b)