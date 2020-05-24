# 컨테이너 운반
# 10/10

T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))

    w.sort(reverse=True)
    t.sort(reverse=True)

    l = []
    for m in t:
        for n in w:
            if m >= n:
                l.append(n)
                w.remove(n)
                break

    print(f"#{test_case} {sum(l)}")
