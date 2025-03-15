def func(a, total):
    for i in range(len(a)):
        for j in range(0, len(a)):
            if((total - (a[i]+a[j]) == 100) and i != j):
                x, y = a[i],a[j]
                a.remove(x)
                a.remove(y)
                return a

a = []
for i in range(9):
    a.append(int(input()))
total = sum(a)
a = func(a,total)
a.sort()
for i in range(len(a)):
    print(a[i])

