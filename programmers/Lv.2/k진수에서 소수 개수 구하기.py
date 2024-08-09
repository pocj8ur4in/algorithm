import math


def translate_to_binary(n, k):
    ans = 0
    power = 1
    while n > 0:
        remainder = n % k
        ans += remainder * power
        n //= k
        power *= 10
    return ans


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = []
    for num in str(translate_to_binary(n, k)).split("0"):
        if num == "":
            continue
        if is_prime(int(num)):
            answer.append(num)

    return len(answer)

# 테스트 1 〉	통과 (134.30ms, 10.2MB)
# 테스트 2 〉	통과 (0.03ms, 10.4MB)
# 테스트 3 〉	통과 (0.03ms, 10.4MB)
# 테스트 4 〉	통과 (0.03ms, 10.3MB)
# 테스트 5 〉	통과 (0.03ms, 10.3MB)
# 테스트 6 〉	통과 (0.03ms, 10.3MB)
# 테스트 7 〉	통과 (0.03ms, 10.2MB)
# 테스트 8 〉	통과 (0.03ms, 10.2MB)
# 테스트 9 〉	통과 (0.04ms, 10.4MB)
# 테스트 10 〉	통과 (0.04ms, 10.4MB)
# 테스트 11 〉	통과 (0.03ms, 10.3MB)
# 테스트 12 〉	통과 (0.03ms, 10.3MB)
# 테스트 13 〉	통과 (0.03ms, 10.4MB)
# 테스트 14 〉	통과 (0.03ms, 10.3MB)
# 테스트 15 〉	통과 (0.03ms, 10.4MB)
# 테스트 16 〉	통과 (0.03ms, 10.2MB)