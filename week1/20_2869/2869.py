import math

a = list(map(int, input().split()))
d = math.ceil((a[2]-a[0]) / (a[0]-a[1])) +1
print(d)