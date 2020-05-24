# 전자키트
# 10/10

import itertools


def search(table, numbers, index):
    global N
    x = numbers[index - 1]

    if index == N - 1:
        return table[x][0] + table[0][numbers[0]]

    y = numbers[index]
    return table[x][y] + search(table, numbers, index + 1)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    p = itertools.permutations([x for x in range(1, N)], N - 1)
    m = min([search(table, list(l), 1) for l in list(p)])

    print(f"#{test_case} {m}")
