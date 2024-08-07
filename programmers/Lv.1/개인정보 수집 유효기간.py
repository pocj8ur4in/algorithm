def solution(today, terms, privacies):
    answer = []

    dict_terms = {name: limit for name, limit in (term.split(" ") for term in terms)}
    arr_privacies = [privacy.split(" ") for privacy in privacies]
    arr_today = [int(date) for date in today.split(".")]

    for indext_arr_privacies in range(0, len(arr_privacies)):
        arr_privacy = [int(date) for date in arr_privacies[indext_arr_privacies][0].split(".")]
        arr_privacy[1] += int(dict_terms.get(arr_privacies[indext_arr_privacies][1]))
        arr_privacy[0], arr_privacy[1] = arr_privacy[0] + (arr_privacy[1] - 1) // 12, (arr_privacy[1] - 1) % 12 + 1

        if (arr_today[0], arr_today[1], arr_today[2]) < (arr_privacy[0], arr_privacy[1], arr_privacy[2]):
            continue

        answer.append(indext_arr_privacies + 1)

    return answer

# 테스트 1 〉	통과 (0.03ms, 10.4MB)
# 테스트 2 〉	통과 (0.04ms, 10.4MB)
# 테스트 3 〉	통과 (0.03ms, 10.4MB)
# 테스트 4 〉	통과 (0.03ms, 10.5MB)
# 테스트 5 〉	통과 (0.06ms, 10.3MB)
# 테스트 6 〉	통과 (0.05ms, 10.5MB)
# 테스트 7 〉	통과 (0.05ms, 10.4MB)
# 테스트 8 〉	통과 (0.06ms, 10.4MB)
# 테스트 9 〉	통과 (0.10ms, 10.4MB)
# 테스트 10 〉	통과 (0.10ms, 10.4MB)
# 테스트 11 〉	통과 (0.10ms, 10.4MB)
# 테스트 12 〉	통과 (0.33ms, 10.4MB)
# 테스트 13 〉	통과 (0.18ms, 10.3MB)
# 테스트 14 〉	통과 (0.18ms, 10.4MB)
# 테스트 15 〉	통과 (0.10ms, 10.4MB)
# 테스트 16 〉	통과 (0.18ms, 10.4MB)
# 테스트 17 〉	통과 (0.17ms, 10.4MB)
# 테스트 18 〉	통과 (0.19ms, 10.2MB)
# 테스트 19 〉	통과 (0.18ms, 10.3MB)
# 테스트 20 〉	통과 (0.18ms, 10.2MB)
