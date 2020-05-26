# 전기버스2
# 5/10

T = int(input())
for test_case in range(1, T + 1):
    N, *M = list(map(int, input().split()))

    index = 0
    count = -1
    battery = 0

    path = []
    while index < N - 1:
        path.append(M[index])
        if battery == 0:
            battery = max(path)
            count += 1
            path = []
        index += 1
        battery -= 1

    print(f"#{test_case} {count}")
