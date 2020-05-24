# 퀵 정렬
# 10/10


def quick_sort(arr, method="hoare"):
    def sort(low, high):
        if low < high:
            mid = partition(low, high, method)
            sort(low, mid - 1)
            sort(mid + 1, high)
        return arr

    def partition(low, high, method):
        if method == "hoare":
            return hoare_partition(low, high)
        elif method == "lomuto":
            return lomuto_partition(low, high)

    def hoare_partition(low, high):
        p = arr[low]
        i = low + 1
        j = high

        while i <= j:
            while i <= j and arr[i] <= p:
                i += 1
            while i <= j and arr[j] >= p:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]
        return j

    def lomuto_partition(low, high):
        x = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= x:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    return sort(0, len(arr) - 1)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    arr = quick_sort(arr)

    print(f"#{test_case} {arr[N // 2]}")
