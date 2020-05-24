# 화물 도크
# 10/10

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    l = [tuple(map(int, input().split())) for _ in range(N)]

    l.sort(key=lambda x: x[1])

    queue = []
    for i, (_, e) in enumerate(l):
        if queue:
            if queue[len(queue) - 1][1] > l[i][0]:
                continue
        for s, _ in l[i + 1 :]:
            if s >= e:
                break
        queue.append(l[i])

    print(f"#{test_case} {len(queue)}")
