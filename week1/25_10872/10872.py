def recursive(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*recursive(n-1)


n = int(input())
a = recursive(n)
print(a)
