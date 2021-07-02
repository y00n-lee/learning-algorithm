def solution(s):
    answer = []

    # 문자 { } 제거
    s = s.replace('{', '').replace('}', '')

    arr = list(map(int, s.split(',')))  # ,(콤마)를 기준으로 나눠서 숫자값 리스트에 저장
    set_arr = set(arr)  # set으로 중복 제거

    count_list = [0] * (max(set_arr) + 1)  # 가장 큰 값을 기준으로 리스트 생성

    count_dict = {}

    # 카운트 딕셔너리 초기화
    for i in set_arr:
        count_dict[i] = 0

    # 카운트 딕셔너리의 값에 중복 횟수 저장
    for i in arr:
        count_dict[i] += 1

    # 반복이 많이 된 값부터 출력
    for _ in range(len(set_arr)):
        max_value = max(count_dict.values())
        for k, v in count_dict.items():
            if v == max_value:
                answer.append(k)
                count_dict[k] = -1

    return answer