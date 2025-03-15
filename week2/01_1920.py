def binary_search(a,left,right, target):
    if left > right:
        print(0)
        return
    mid = (left + right) //2

    if a[mid] == target:
        print(1)
        return
    elif a[mid] < target:
        binary_search(a,mid+1,right,target)
    else:
        binary_search(a,left,mid-1,target)


n = int(input())
a = []
a = list(map(int, input().split()))
a.sort()
m = int(input())
b = []
b= list(map(int, input().split()))

for i in range(m):
    binary_search(a,0,len(a)-1,b[i])