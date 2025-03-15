num = int(input())
for i in range(num):
    a=input().split()
    num1=int(a[0])
    word=a[1]
    for j in range (0,len(word)):
        for k in range (0,num1):
            print(word[j], end="")
    print('')