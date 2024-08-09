def solution(N, stages):
    answer = []
    clear = []
    cnt = len(stages)

    for target in range(1, N + 1):
        clear.append((target, stages.count(target) / cnt if cnt != 0 else 0))
        cnt -= stages.count(target)

    clear.sort(key=lambda x: (-x[1], x[0]))
    answer = [stage[0] for stage in clear]

    return answer