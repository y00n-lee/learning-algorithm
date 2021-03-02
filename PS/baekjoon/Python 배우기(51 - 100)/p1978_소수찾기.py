def check(p_list):
    count = 0
    for num in p_list:
        if num == 1 or num < 1:
            continue
        if num == 2:
            count += 1

        else:
            flag = True
            for n in range(2,num):
                if num % n == 0:
                    flag = False
                    break
            if flag:
                count += 1

    return count


def solve():
    n = int(input())
    p = list(map(int, input().split()))

    return check(p)


print(solve())