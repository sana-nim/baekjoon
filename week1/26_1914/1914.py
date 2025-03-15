def move(n, start, end, sub):
    if n == 1:
        print(start, end)
        return

    move(n-1, start, sub, end)
    print(start, end)
    move(n-1, sub, end, start)

    return

n = int(input())

if n > 20:
    print(2**n-1)
else:
    print(2**n-1)
    move(n, 1, 3, 2)
