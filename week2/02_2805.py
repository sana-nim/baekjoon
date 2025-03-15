def binarySearch(a, left, right, target):
    result = 0

    while left <= right:
        mid = (left + right) // 2

        total = 0
        for tree in a:
            if tree > mid:
                total += (tree - mid)

        if total >= target:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

n, m = map(int, input().split())
a = list(map(int, input().split()))

result = binarySearch(a, 0, max(a), m)
print(result)
