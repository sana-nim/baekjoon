def func(a, start_x, end_x, start_y, end_y, check):
    value = a[start_x][start_y]
    size = end_x - start_x

    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            if a[i][j] != value:
                if size == 1:
                    return

                mid = size // 2
                func(a, start_x, start_x + mid, start_y, start_y + mid, check)  # 왼쪽 위
                func(a, start_x, start_x + mid, start_y + mid, end_y, check)     # 오른쪽 위
                func(a, start_x + mid, end_x, start_y, start_y + mid, check)     # 왼쪽 아래
                func(a, start_x + mid, end_x, start_y + mid, end_y, check)       # 오른쪽 아래
                return

    if value == 0:
        check[0] += 1
    else:
        check[1] += 1

n = int(input())
a = []
check = [0, 0]

for i in range(n):
    a.append(list(map(int, input().split())))

func(a, 0, n, 0, n, check)

print(check[0])
print(check[1])
