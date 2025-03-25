def b_search(a, c, low, high, result):
    if low > high:
        return result

    mid = (low+high)//2
    cnt = 1
    last_installed = a[0]

    for i in range(1,len(a)):
        if a[i] - last_installed >= mid:
            cnt += 1
            last_installed = a[i]
        if cnt == c:
            break

    if cnt >= c:
        result = mid
        return b_search(a,c,mid+1, high, result)
    else:
        return b_search(a,c,low,mid-1,result)

n = list(map(int,input().split()))
a = []
for i in range(n[0]):
    a.append(int(input()))
a.sort()
result = b_search(a,n[1],1,a[-1]-a[0],0)
print(result)