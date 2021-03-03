a, b = input().split()
tmp1 = ""
tmp2 = ""
for i in range(1,len(a)+1):
    tmp1 += a[-i]
    tmp2 += b[-i]

a, b = int(tmp1), int(tmp2)

if a > b:
    print(a)

else:
    print(b)