# 병합 정렬
# 10/10


def merge(left, right):
    global c

    li, ri = 0, 0
    ln, rn = len(left), len(right)
    result = [0] * (ln + rn)
    index = 0

    if left[-1] > right[-1]:
        c += 1

    while li < ln and ri < rn:
        if left[li] <= right[ri]:
            result[index] = left[li]
            index += 1
            li += 1
        else:
            result[index] = right[ri]
            index += 1
            ri += 1

    if li < ln:
        while li < ln:
            result[index] = left[li]
            index += 1
            li += 1
    if ri < rn:
        while ri < rn:
            result[index] = right[ri]
            index += 1
            ri += 1

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    l = merge_sort(arr[:mid])
    r = merge_sort(arr[mid:])

    return merge(l, r)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    c = 0
    r = merge_sort(arr)

    print(f"#{test_case} {r[N//2]} {c}")
