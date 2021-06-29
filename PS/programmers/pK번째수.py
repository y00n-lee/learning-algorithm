def solution(array, commands):
    answer = []
    for x in range(len(commands)):
        i, j, k = commands[x][0], commands[x][1], commands[x][2]
        array_split = array[i - 1:j]
        array_split.sort()
        answer.append(array_split[k - 1])

    return answer