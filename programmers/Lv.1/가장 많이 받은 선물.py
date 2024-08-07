def solution(friends, gifts):
    next = [[0 for i in range(len(friends))] for i in range(len(friends))]
    next_gift = [0 for i in range(len(friends))]

    for gift in gifts:
        next[friends.index(gift.split(" ")[0])][friends.index(gift.split(" ")[1])] += 1

    for i in range(0, len(friends)):
        for j in range(0, len(friends)):
            if next[i][j] > next[j][i]:
                next_gift[i] += 1
            elif next[i][j] == next[j][i]:
                if (sum(next[i]) - sum(next[line][i] for line in range(len(friends))))\
                        > (sum(next[j]) - sum(next[line][j] for line in range(len(friends)))):
                    next_gift[i] += 1

    return max(next_gift)

# 테스트 1 〉	통과 (0.05ms, 10.2MB)
# 테스트 2 〉	통과 (0.09ms, 10.3MB)
# 테스트 3 〉	통과 (0.26ms, 10.3MB)
# 테스트 4 〉	통과 (0.56ms, 10.2MB)
# 테스트 5 〉	통과 (1.14ms, 10.3MB)
# 테스트 6 〉	통과 (0.54ms, 10.3MB)
# 테스트 7 〉	통과 (3.18ms, 10.2MB)
# 테스트 8 〉	통과 (2.63ms, 10.4MB)
# 테스트 9 〉	통과 (6.28ms, 10.4MB)
# 테스트 10 〉	통과 (5.96ms, 10.7MB)
# 테스트 11 〉	통과 (5.74ms, 10.5MB)
# 테스트 12 〉	통과 (4.01ms, 10.6MB)
# 테스트 13 〉	통과 (15.45ms, 10.7MB)
# 테스트 14 〉	통과 (10.08ms, 10.6MB)
# 테스트 15 〉	통과 (14.90ms, 10.6MB)
# 테스트 16 〉	통과 (18.94ms, 10.9MB)
# 테스트 17 〉	통과 (0.49ms, 10.3MB)
# 테스트 18 〉	통과 (6.38ms, 10.7MB)
# 테스트 19 〉	통과 (31.79ms, 10.6MB)
# 테스트 20 〉	통과 (28.11ms, 10.4MB)
