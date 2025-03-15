a = input().split()
n1=list();
n2=list();

for i in range(2,-1,-1):
    n1.append(a[0][i])
    n2.append(a[1][i])

x = ''.join(n1)
y = ''.join(n2)

if(x > y):
    print(x)
else:
    print(y)