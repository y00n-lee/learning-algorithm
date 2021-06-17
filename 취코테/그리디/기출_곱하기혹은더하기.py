s = input()

result = int(s[0])
for i in s[1:]:
    i = int(i)
    # if result * i == 0 or result * i < result + i:
    if i <= 1 or result <= 1: # 위의 주석 처리한 조건과 결과가 같으나 더 간결
        result += i

    else:
        result *= i

print(result)

