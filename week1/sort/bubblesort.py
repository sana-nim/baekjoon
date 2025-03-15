from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j + 1] = a[j + 1], a[j]


if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))

    bubble_sort(a)
    for i in range(n):
        print(a[i])
