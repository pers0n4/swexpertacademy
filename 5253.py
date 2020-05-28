# 접두어 검색
# 10/10

T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    A = [input() for _ in range(N)]
    B = [input() for _ in range(M)]

    is_prefix = [False] * M
    for i, b in enumerate(B):
        for a in A:
            if a.startswith(b):
                is_prefix[i] = True
                break

    print(f"#{test_case} {sum(is_prefix)}")
