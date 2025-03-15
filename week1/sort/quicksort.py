def partition(left, right):
    pivot = a[left]
    i = left
    j = right

    while(i < j):
        while (i < right and a[i] <= pivot):i+=1
        while (j > left and a[j] > pivot): j-=1
        if i < j:
            a[i], a[j] = a[j], a[i]

    a[left], a[j] = a[j], a[left]
    return j

def quicksort(left, right):
    if (left < right):
        j = partition(left,right)
        quicksort(left, j-1)
        quicksort(j+1, right)

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))

    quicksort(0,len(a)-1)