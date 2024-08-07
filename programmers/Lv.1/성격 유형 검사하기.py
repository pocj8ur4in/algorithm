def solution(survey, choices):
    answer = ''
    arr_personality = ["R", "T", "C", "F", "J", "M", "A", "N"]
    dict_personality = {personality: 0 for personality in arr_personality}

    for index_survey in range(0, len(survey)):
        if 1 <= choices[index_survey] < 4:
            dict_personality[survey[index_survey][0]] += 4 - choices[index_survey]
        elif 4 <= choices[index_survey] <= 7:
            dict_personality[survey[index_survey][1]] += choices[index_survey] - 4

    for half in range(0, len(dict_personality) // 2):
        if dict_personality[arr_personality[half * 2]] == dict_personality[arr_personality[half * 2 + 1]]:
            answer += arr_personality[half * 2]
        elif dict_personality[arr_personality[half * 2]] > dict_personality[arr_personality[half * 2 + 1]]:
            answer += arr_personality[half * 2]
        else:
            answer += arr_personality[half * 2 + 1]

    return answer

# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.02ms, 10.4MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.3MB)
# 테스트 8 〉	통과 (0.03ms, 10.2MB)
# 테스트 9 〉	통과 (0.03ms, 10.3MB)
# 테스트 10 〉	통과 (0.03ms, 10.4MB)
# 테스트 11 〉	통과 (0.06ms, 10.2MB)
# 테스트 12 〉	통과 (0.08ms, 10.1MB)
# 테스트 13 〉	통과 (0.11ms, 10.2MB)
# 테스트 14 〉	통과 (0.18ms, 10.2MB)
# 테스트 15 〉	통과 (0.21ms, 10.2MB)
# 테스트 16 〉	통과 (0.22ms, 10.2MB)
# 테스트 17 〉	통과 (0.23ms, 10.1MB)
# 테스트 18 〉	통과 (0.23ms, 10.1MB)
# 테스트 19 〉	통과 (0.45ms, 10.3MB)
# 테스트 20 〉	통과 (0.22ms, 10.3MB)
