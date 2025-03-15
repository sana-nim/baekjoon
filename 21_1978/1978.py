import math
def isPrime(n):
    end = int(math.sqrt(n))
    if  n == 1:
        return False
    for i in range(2,end):
        if n % i == 0:
            return False
    return True

n = input().split()
prime = 0
a = list(map(int, input().split()))
for i in range(len(a)):
    if(isPrime(a[i])):
        print(a[i])
        prime+=1

print(prime)
