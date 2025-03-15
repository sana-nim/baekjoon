a=int(input())
b=int(input())
c=int(input())
mul = []
arr = [0] * 10
mul = list(str(a*b*c))

for i in range(len(mul)):
    arr[int(mul[i])] += 1

for i in range(len(arr)):
    print(arr[i])
