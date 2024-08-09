numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def solution(s):
    for number in numbers:
        s = s.replace(number, str(numbers.index(number)))

    answer = int(s)
    return answer

# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.02ms, 10.1MB)
# 테스트 3 〉	통과 (0.02ms, 10.3MB)
# 테스트 4 〉	통과 (0.03ms, 10.1MB)
# 테스트 5 〉	통과 (0.02ms, 10MB)
# 테스트 6 〉	통과 (0.02ms, 10.3MB)
# 테스트 7 〉	통과 (0.03ms, 10.1MB)
# 테스트 8 〉	통과 (0.03ms, 10.3MB)
# 테스트 9 〉	통과 (0.02ms, 10MB)
# 테스트 10 〉	통과 (0.02ms, 10.3MB)
