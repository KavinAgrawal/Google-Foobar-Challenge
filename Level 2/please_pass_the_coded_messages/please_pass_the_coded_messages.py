from itertools import combinations 
def solution(l):
    l.sort(reverse = True)
    for i in reversed(range(1, len(l) + 1)):
        for x in combinations(l, i):
            if sum(x) % 3 == 0: return int(''.join(map(str, x)))
    return 0

print(solution([3, 1, 4, 1, 5, 9]))