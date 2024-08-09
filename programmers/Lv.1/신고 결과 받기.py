def solution(id_list, report, k):
    report = list(set(report))
    answer = []
    from_id = {name: [] for name in id_list}
    to_id = {name: 0 for name in id_list}

    for singo in report:
        singo_split = singo.split(" ")
        to_id[singo.split(" ")[1]] += 1
        from_id[singo.split(" ")[0]].append(singo.split(" ")[1])

    for key, value in from_id.items():
        answer_count = 0
        for name in value:
            if to_id[name] < k:
                continue
            answer_count += 1
        answer.append(answer_count)

    return answer

# 테스트 1 〉	통과 (0.02ms, 10MB)
# 테스트 2 〉	통과 (0.05ms, 10.3MB)
# 테스트 3 〉	통과 (259.60ms, 39.1MB)
# 테스트 4 〉	통과 (0.05ms, 10.3MB)
# 테스트 5 〉	통과 (0.06ms, 10.2MB)
# 테스트 6 〉	통과 (1.60ms, 10.6MB)
# 테스트 7 〉	통과 (2.52ms, 10.6MB)
# 테스트 8 〉	통과 (3.14ms, 11MB)
# 테스트 9 〉	통과 (113.54ms, 23.8MB)
# 테스트 10 〉	통과 (100.68ms, 23.8MB)
# 테스트 11 〉	통과 (247.25ms, 39.2MB)
# 테스트 12 〉	통과 (0.35ms, 10.3MB)
# 테스트 13 〉	통과 (0.35ms, 10.2MB)
# 테스트 14 〉	통과 (113.16ms, 22.4MB)
# 테스트 15 〉	통과 (138.80ms, 32.6MB)
# 테스트 16 〉	통과 (0.35ms, 10.2MB)
# 테스트 17 〉	통과 (0.34ms, 10.1MB)
# 테스트 18 〉	통과 (1.03ms, 10.2MB)
# 테스트 19 〉	통과 (1.20ms, 10.3MB)
# 테스트 20 〉	통과 (106.33ms, 22.4MB)
# 테스트 21 〉	통과 (168.26ms, 32.6MB)
# 테스트 22 〉	통과 (0.01ms, 10MB)
# 테스트 23 〉	통과 (0.01ms, 10.1MB)
# 테스트 24 〉	통과 (0.01ms, 10.2MB)
