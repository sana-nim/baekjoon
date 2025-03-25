n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

cnt = 1
flag = a[-1]

for i in range(n-1,-1,-1):

    if a[i] > flag:
        cnt += 1
        flag = a[i]

print(cnt)