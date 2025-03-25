def func(a, b, c):
    if b == 0:
        return 1

    half = func(a, b // 2, c) % c

    if b % 2 == 0:
        return (half * half) % c
    else:
        return (half * half * a) % c

a = list(map(int, input().split()))
result = func(a[0], a[1], a[2])
print(result)
