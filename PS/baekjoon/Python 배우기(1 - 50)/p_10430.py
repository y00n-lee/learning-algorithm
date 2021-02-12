# 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
# (2 ≤ A, B, C ≤ 10000)

try:
    a, b, c = map(int, input().split())
    while(a<2 or a>10000 or b<2 or b>10000 or c<2 or c>10000):
        print("범위를 맞춰주세요. (2 ≤ A, B, C ≤ 10000)")
        a, b, c = map(int, input().split())
    print((a+b)%c)
    print(((a%c)+(b%c))%c)
    print((a*b)%c)
    print(((a%c)*(b%c))%c)
except:
    print("숫자를 세개만 입력해주세요.")

