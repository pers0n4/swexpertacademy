# 최소합
# 9/10


def search(table, x, y, total, result):
    total += table[y][x]

    l = len(table) - 1
    if y == l and x == l:
        result.append(total)

    if y != l:
        search(table, x, y + 1, total, result)
    if x != l:
        search(table, x + 1, y, total, result)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    r = []
    search(table, 0, 0, 0, r)
    print(f"#{test_case} {min(r)}")
