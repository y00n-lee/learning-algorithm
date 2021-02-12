try:
    n = int(input())
    while(n<=0):
        print("양의 정수를 입력하세요.")
        n = int(input())
except ValueError:
    print("양의 정수를 입력하세요.")


a = []
b = []
for i in range(n):
    try:
        x, y = map(int, input().split())
        while(x<=0 or x >10 or y<=0 or y>10):
            print("두 수 모두 0보다 크고 10보다 작은 수로 입력하세요.")
            x, y = map(int, input().split())
        a.append(x)
        b.append((y))
    except:
        print("숫자(정수)만 입력하세요.")

for i in range(n):
    print(f"Case #{i+1}: {a[i]+b[i]}")