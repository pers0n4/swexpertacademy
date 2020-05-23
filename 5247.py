# 연산
# pass 3/10


def calc(begin, end, count):
    queue = []

    for b in begin:
        if b == end:
            return count

        if 0 < b + 1 < 1000000:
            queue.append(b + 1)
            if 0 < b * 2 < 1000000:
                queue.append(b * 2)
        if 0 < b - 1 < 1000000:
            queue.append(b - 1)
            if 0 < b - 10 < 1000000:
                queue.append(b - 10)

    return calc(queue, end, count + 1)


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    count = calc([N], M, 0)

    print(f"#{test_case} {count}")
