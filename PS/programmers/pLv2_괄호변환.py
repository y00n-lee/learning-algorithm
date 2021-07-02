def solution(p):
    answer = perfect_bracket(p)

    return answer


def perfect_bracket(p):
    if not len(p):
        return p

    left_bracket = 0
    right_bracket = 0
    u, v = '', ''

    if p[0] == '(':
        left_bracket += 1

    elif p[0] == ')':
        right_bracket += 1

    u += p[0]

    for i in range(1, len(p)):
        if left_bracket == right_bracket:
            v += p[i]

        else:
            if p[i] == '(':
                left_bracket += 1
            else:
                right_bracket += 1
            u += p[i]

    if u[0] == '(':
        return u + perfect_bracket(v)

    else:
        tmp = '(' + perfect_bracket(v) + ')'
        new_u = ''

        for i in u[1:-1]:
            if i == '(':
                new_u += ')'

            else:
                new_u += '('

        return tmp + new_u
