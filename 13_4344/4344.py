row = int(input())
n=0
sum=[]
arr=[]
result=[]
percent=[]
for i in range(row):
    arr.append(list(map(int, input().split())))

for i in range(row):
    n = 0
    for j in range(1,len(arr[i])):
        n+=arr[i][j];
    sum.append(n)

for i in range(row):
    n = 0
    for j in range(1, len(arr[i])):
        if(arr[i][j] > sum[i]/arr[i][0]):
            n+=1
    result.append(n*100)
    
for i in range(row):
    percent.append(result[i]/arr[i][0])
    print("%.3f%%" % (percent[i]));

