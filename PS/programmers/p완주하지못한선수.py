def solution(participant, completion):
    answer = 0
    participant.sort()
    completion.sort()

    part_dict = {0: participant[0]}
    comp_dict = {}
    for i, name in enumerate(completion):
        comp_dict[i] = name
        part_dict[i + 1] = participant[i + 1]

    for k, name in comp_dict.items():
        if part_dict.get(k) == name:
            del part_dict[k]
        elif part_dict.get(k+1) == name:
            del part_dict[k+1]

        else:
            answer = name
            break

    if not answer:
        for v in part_dict.values():
            answer = v

    return answer


print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))