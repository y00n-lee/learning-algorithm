def solution(n, lost, reserve):
    answer = 0
    cloth = [1] * n

    for i in lost:
        cloth[i - 1] -= 1

    for j in reserve:
        cloth[j - 1] += 1

    for idx in range(len(cloth)):
        if not cloth[idx]:
            if idx == 0 and cloth[idx + 1] == 2:
                cloth[idx] += 1
                cloth[idx + 1] -= 1

            elif idx == len(cloth) - 1 and cloth[idx - 1] == 2:
                cloth[idx] += 1
                cloth[idx - 1] -= 1

            elif not idx == 0 and cloth[idx - 1] == 2:
                cloth[idx] += 1
                cloth[idx - 1] -= 1

            elif not idx == len(cloth) - 1 and cloth[idx + 1] == 2:
                cloth[idx] += 1
                cloth[idx + 1] -= 1

    for i in cloth:
        if i > 0:
            answer += 1

    return answer