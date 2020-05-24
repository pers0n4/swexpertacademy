# 이진 탐색
# 5/10


def binary_search(value, target, low, high):
    if low > high:
        return 0

    mid = (low + high) // 2
    if target[mid] > value:
        return binary_search(value, target, low, mid - 1)
    elif target[mid] < value:
        return binary_search(value, target, mid + 1, high)
    else:
        return mid + 1


T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    print(A, B)

    r = list(map(lambda v: binary_search(v, B, 0, len(B) - 1), A))
    c = sum(list(map(lambda x: 1 if x else 0, r)))

    print(f"#{test_case} {c}")
