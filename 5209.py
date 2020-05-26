# 최소 생산 비용
# 10/10


def dfs(G):
    check = [False] * N
    mini = sum([sum(l) for l in G])

    def search(k, cost):
        nonlocal mini

        if cost > mini:
            return

        if k == N:
            if cost < mini:
                mini = cost
            return

        for i in range(N):
            if check[i] is False:
                check[i] = True
                search(k + 1, cost + G[k][i])
                check[i] = False

        return mini

    return search(0, 0)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]

    c = dfs(V)

    print(f"#{test_case} {c}")
