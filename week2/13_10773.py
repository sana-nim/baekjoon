n = int(input())
stack = []
for i in range(n):
    ready = int(input())
    if ready == 0:
        stack.pop()
    else:
        stack.append(ready)
print(sum(stack))