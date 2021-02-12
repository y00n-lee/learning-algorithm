a = int(input())
while a<100 or a>=1000:
    print("세 자리수를 입력해 주세요.")
    a = int(input())

b = input()
while int(b)<100 or int(b)>=1000:
    print("세 자리수를 입력해 주세요.")
    b = input()
b = b[::-1]

for i in range(3):
    print(a * int(b[i]))
print(a * int(b[::-1]))


