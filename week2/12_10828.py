def push(stack, x):
    stack.append(x)

def pop(stack):
    if len(stack) == 0:
        return -1
    return stack.pop()

def size(stack):
    return len(stack)

def empty(stack):
    if len(stack) == 0:
        return  1
    else:
        return 0


def top(stack):
    if len(stack) == 0:
        return -1
    return stack[-1]


n = int(input())
stack = []
result = []

for _ in range(n):
    command = input().strip().split()

    if command[0] == 'push':
        push(stack, int(command[1]))
    elif command[0] == 'pop':
        result.append(pop(stack))
    elif command[0] == 'size':
        result.append(size(stack))
    elif command[0] == 'empty':
        result.append(empty(stack))
    elif command[0] == 'top':
        result.append(top(stack))

print("\n".join(map(str, result)))