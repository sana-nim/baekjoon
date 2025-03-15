T = int(input())

for i in range(T):
    VPS = input().strip()
    cnt = 0
    isVPS = True

    for j in range(len(VPS)):
        if VPS[j] == "(":
            cnt+=1
        else:
            cnt-=1
            if cnt < 0:
                isVPS = False
                break

    if isVPS and cnt == 0:
        print("YES")
    else:
        print("NO")