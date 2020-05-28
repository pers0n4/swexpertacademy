# 공통 단어 검색
# 10/10

T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    A = [input() for _ in range(N)]
    B = [input() for _ in range(M)]

    A = set(A)
    B = set(B)

    print(f"#{test_case} {len(A & B)}")
