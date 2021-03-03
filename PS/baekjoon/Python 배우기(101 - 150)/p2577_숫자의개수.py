a = int(input())
b = int(input())
c = int(input())

number = a * b * c

count = [0,0,0,0,0,0,0,0,0,0]   # 숫자 개수를 세기 위한 리스트

for n in str(number):
    index = int(n)
    count[index] += 1

for ans in count:
    print(ans)