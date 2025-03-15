def dif(value):
    numlist = [int(i) for i in value]
    length = len(numlist)
    if length == 1:
        return True
    d = numlist[0] - numlist[1]
    for i in range(1, length - 1):
        if d != numlist[i] - numlist[i + 1]:
            return False
    return True


cnt = 0
num = int(input())

for i in range(1, num + 1):
    if dif(str(i)):
        cnt += 1

print(cnt)
